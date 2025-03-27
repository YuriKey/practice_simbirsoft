# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import pytest
#
#
# @pytest.fixture(scope='function')
# def browser():
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_browser = webdriver.Chrome(options=chrome_options)
#     chrome_browser.implicitly_wait(3)
#     yield chrome_browser
#     chrome_browser.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import pytest


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
