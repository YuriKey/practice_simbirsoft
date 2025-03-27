"""Local launch"""

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


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pytest


"""CI/CD launch"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(3)
    yield chrome_browser
    chrome_browser.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pytest
#
#
# @pytest.fixture(scope="function")
# def browser():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")  # Используем новый headless режим
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--remote-debugging-port=9222")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920,1080")
#
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.implicitly_wait(10)  # Добавляем неявное ожидание
#
#     yield driver
#     driver.quit()
