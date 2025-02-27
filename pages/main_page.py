from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    @staticmethod
    def js_click(driver, locator):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].click();", element)

    def fill_form(self, data):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(data.name)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(data.password)
        self.element_is_visible(self.locators.MILK_CHECKBOX).click()
        self.element_is_visible(self.locators.COFFEE_CHECKBOX).click()
        self.element_is_visible(self.locators.RBUTTON_YELLOW).click()
        self.js_click(self.driver, self.locators.AUTO_TYPE_MENU)
        self.element_is_visible(self.locators.AUTO_TYPE).click()
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(data.email)
        self.element_is_present(self.locators.MESSAGE_FIELD).send_keys(data.message)
