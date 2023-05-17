from typing import Dict
from selene import Browser


def current_browser_cookie(browser: Browser) -> str:
    """
    Get current browser cookie

    Args:
        browser (Browser): The browser instance to get cookies from.

    Returns:
        str: A string representation of the cookies.

    Example:
        >>> browser = Browser()
        >>> cookies = current_browser_cookie(browser)
    """
    cookies = browser.config.driver.get_cookies()

    cookies_dict: Dict[str, str] = {}

    for cookie in cookies:
        cookies_dict[cookie['name']] = cookie['value']

    cookie_val = '; '.join([f"{name}={value}" for name, value in cookies_dict.items()])
    return cookie_val
