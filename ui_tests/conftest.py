import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""Local launch"""


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(3)
    yield chrome_browser
    chrome_browser.quit()

"""CI/CD launch"""


# @pytest.fixture(scope="function")
# def browser():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_browser = webdriver.Chrome(options=chrome_options)
#     chrome_browser.implicitly_wait(3)
#     yield chrome_browser
#     chrome_browser.quit()
