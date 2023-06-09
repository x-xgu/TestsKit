import functools
import inspect
from typing import Callable, Literal

import requests
import urllib3
from loguru import logger
from requests import Request, RequestException
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

RequestMethod = Literal['get', 'post', 'put', 'delete', 'head', 'options', 'trace']

COMMON_HEADERS = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
}


class HttpDecorator:
    """
    A decorator class that sends HTTP requests to a specified URL.

    Args:
        url (str): The URL to send the request to.
        method (RequestMethod, optional): The HTTP method to use. Defaults to 'get'.

    Example:
        >>> @HttpDecorator(url='https://jsonplaceholder.typicode.com/posts/1')
        >>> def get_post():
        >>>     return {'params': {'userId': 1}}
        >>>
        >>> response = get_post()
    """

    def __init__(
            self,
            url: str,
            method: RequestMethod = 'get'
    ) -> None:
        self.url = url
        self.method = method
        self.func_return = {}
        self.func_im_self = None

    def __call__(
            self,
            func: Callable
    ) -> Callable:
        """
        The decorator function that sends the HTTP request.

        Args:
            func (Callable): The function to decorate.

        Returns:
            Callable: The decorated function.

        Example:
            >>> @HttpDecorator(url='https://jsonplaceholder.typicode.com/posts/1')
            >>> def get_post():
            >>>     return {'params': {'userId': 1}}
            >>>
            >>> response = get_post()
        """
        self.func = func
        self.is_class = False

        try:
            if inspect.getfullargspec(self.func).args[0] == 'self':
                self.is_class = True
        except IndexError as e:
            logger.error(f'IndexError: {e}')
            pass

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            The wrapper function that sends the HTTP request.

            Args:
                *args: The positional arguments to pass to the decorated function.
                **kwargs: The keyword arguments to pass to the decorated function.

            Returns:
                requests.Response: The response from the HTTP request.

            Example:
                >>> @HttpDecorator(url='https://jsonplaceholder.typicode.com/posts/1')
                >>> def get_post():
                >>>     return {'params': {'userId': 1}}
                >>>
                >>> response = get_post()

            Raises:
                RequestException: If the request fails.
            """
            self.func_return = self.func(*args, **kwargs) or {}
            self.func_im_self = args[0] if self.is_class else object

            url = self._create_url()
            session = self._get_session()

            req = Request(self.method, url, **session)
            prepped = req.prepare()

            try:
                res = requests.Session().send(prepped, verify=False)
                res.encoding = res.apparent_encoding
            except RequestException as e:
                logger.error(f'Request failed: {e}')
                raise RequestException(f'Request failed: {e}')
            else:
                return res

        return wrapper

    def _create_url(self) -> str:
        """
        Creates the URL to send the request to.

        Returns:
            str: The URL to send the request to.
        """
        base_url = getattr(self.func_im_self, 'base_url', '')
        url = self.func_return.pop('url', None) or self.url

        return ''.join([base_url, url])

    def _get_session(self) -> dict:
        """
        Gets the session information for the request.

        Returns:
            dict: The session information for the request.
        """
        headers = getattr(self.func_im_self, 'header', {})
        headers.update(COMMON_HEADERS)

        json_data = self.func_return.pop('json', None)
        params = self.func_return.pop('params', None)
        data = self.func_return.pop('data', None)
        files = self.func_return.pop('files', None)

        return {
            'headers': headers,
            'json': json_data,
            'params': params,
            'data': data,
            'files': files
        }
