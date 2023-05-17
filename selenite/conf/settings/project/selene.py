from __future__ import annotations

from pathlib import Path
from typing import Optional, Union, Literal

from pydantic import BaseSettings

BrowserType = Literal['chrome', 'chromium', 'firefox', 'ie', 'edge']

Scope = Literal['session', 'package', 'module', 'class', 'method', 'function']


class SeleneSettings(BaseSettings):
    """
    SeleneSettings is a class that contains settings for Selene framework.

    Args:
        browser_name (BrowserType): Name of the browser to use.
        browser_version (str): Version of the browser to use.
        browser_load_strategy (str): Load strategy of the browser to use.
        browser_management_scope (Scope): Management scope of the browser to use.
        base_url (str): Base URL to use.
        timeout (float): Timeout value to use.
        maximize_window (bool): Whether to maximize the window or not.
        window_width (int): Width of the window to use.
        window_height (int): Height of the window to use.
        headless (bool): Whether to run the browser in headless mode or not.
        incognito (bool): Whether to run the browser in incognito mode or not.
        remote_url (Optional[str]): URL of the remote server to use.
        remote_sessionTimeout (str): Session timeout value to use.
        remote_enableVNC (bool): Whether to enable VNC or not.
        remote_enableVideo (bool): Whether to enable video or not.
        remote_enableLog (bool): Whether to enable log or not.
        remote_videoName (str): Name of the video to use.
        hold_browser_open (bool): Whether to hold the browser open or not.
        save_screenshot_on_failure (bool): Whether to save screenshot on failure or not.
        save_page_source_on_failure (bool): Whether to save page source on failure or not.
        save_case_video_on_failure (bool): Whether to save case video on failure or not.

    Returns:
        SeleneSettings: An instance of SeleneSettings class.

    Example:
        >>> settings = SeleneSettings(
        ...     browser_name='chrome',
        ...     browser_version='91.0.4472.124',
        ...     browser_load_strategy='normal',
        ...     browser_management_scope='session',
        ...     base_url='https://www.google.com',
        ...     timeout=10.0,
        ...     maximize_window=True,
        ...     window_width=1920,
        ...     window_height=1080,
        ...     headless=False,
        ...     incognito=False,
        ...     remote_url='http://localhost:4444/wd/hub',
        ...     remote_sessionTimeout='30s',
        ...     remote_enableVNC=True,
        ...     remote_enableVideo=True,
        ...     remote_enableLog=True,
        ...     remote_videoName='test_video.mp4',
        ...     hold_browser_open=False,
        ...     save_screenshot_on_failure=True,
        ...     save_page_source_on_failure=True,
        ...     save_case_video_on_failure=True
        ... )
    """
    browser_name: BrowserType = ''
    browser_version: str = ''
    browser_load_strategy: str = ''

    browser_management_scope: Scope = ''

    base_url: str = ''

    timeout: float = 5.0

    maximize_window: bool = False
    window_width: int = 1920
    window_height: int = 1080

    headless: bool = False
    incognito: bool = False

    remote_url: Optional[str] = ''
    remote_sessionTimeout: str = ''
    remote_enableVNC: bool = False
    remote_enableVideo: bool = False
    remote_enableLog: bool = False
    remote_videoName: str = ''

    hold_browser_open: bool = False
    save_screenshot_on_failure: bool = False
    save_page_source_on_failure: bool = False
    save_case_video_on_failure: bool = False

    @classmethod
    def in_context(
            cls,
            env: Union[str, Path]
    ) -> SeleneSettings:
        """
        Factory method to init Settings with values from corresponding .env file

        Args:
            env (Union[str, Path]): Path to the .env file.

        Returns:
            SeleneSettings: An instance of SeleneSettings class.

        Example:
            >>> settings = SeleneSettings.in_context('.env')
        """
        return cls(
            _env_file=env
        )

    def update_settings(self, **kwargs) -> SeleneSettings:
        """
        Method to update SeleneSettings instance with new values.

        Args:
            **kwargs: New values to update.

        Returns:
            SeleneSettings: An instance of SeleneSettings class.

        Example:
            >>> settings = SeleneSettings(
            ...     browser_name='chrome',
            ...     browser_version='91.0.4472.124',
            ...     browser_load_strategy='normal',
            ...     browser_management_scope='session',
            ...     base_url='https://www.google.com',
            ...     timeout=10.0,
            ...     maximize_window=True,
            ...     window_width=1920,
            ...     window_height=1080,
            ...     headless=False,
            ...     incognito=False,
            ...     remote_url='http://localhost:4444/wd/hub',
            ...     remote_sessionTimeout='30s',
            ...     remote_enableVNC=True,
            ...     remote_enableVideo=True,
            ...     remote_enableLog=True,
            ...     remote_videoName='test_video.mp4',
            ...     hold_browser_open=False,
            ...     save_screenshot_on_failure=True,
            ...     save_page_source_on_failure=True,
            ...     save_case_video_on_failure=True
            ... )
            >>> updated_settings = settings.update_settings(
            ...     browser_name='firefox',
            ...     timeout=20.0,
            ...     headless=True
            ... )
        """
        return self.copy(update=kwargs)
