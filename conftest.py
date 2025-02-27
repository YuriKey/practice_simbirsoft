import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def open_page(driver, request):
    url = request.param
    driver.get(url)
    yield driver

