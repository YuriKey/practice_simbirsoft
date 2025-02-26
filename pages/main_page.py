from pages.base_page import BasePage
from data.urls import urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(urls.URL)

    @staticmethod
    def interact_with_element(driver, locator, action=None, value=None):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        if action == "click":
            driver.execute_script("arguments[0].click();", element)
        elif action == "send_keys" and value is not None:
            element.send_keys(value)
        elif action is None:
            return element.text

    @staticmethod
    def js_click(driver, locator):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].click();", element)
