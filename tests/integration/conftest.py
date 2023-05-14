import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session')
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def session_browser(chrome_driver):
    browser.config.driver = chrome_driver
    yield
