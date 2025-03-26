from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(3)
    yield chrome_browser
    chrome_browser.quit()

