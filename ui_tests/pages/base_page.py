from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, browser: WebDriver, url=None):
        self.url = url
        self.browser = browser

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def open(self, url):
        self.browser.get(url)

    def click(self, args):
        self.find_element(args).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))
