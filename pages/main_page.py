from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):
    locators = MainPageLocators()

    @staticmethod
    def js_click(driver, locator):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].click();", element)

    def fill_form(self, data):
        with allure.step('Заполнение поля "Имя"'):
            self.element_is_visible(self.locators.NAME_FIELD).send_keys(data.name)
        with allure.step('Заполнение поля "Пароль"'):
            self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(data.password)
        with allure.step('Выбор напитка'):
            self.element_is_visible(self.locators.MILK_CHECKBOX).click()
            self.element_is_visible(self.locators.COFFEE_CHECKBOX).click()
        with allure.step('Выбор цвета'):
            self.element_is_visible(self.locators.RBUTTON_YELLOW).click()
        with allure.step('Заполнение поля "Do you like automation?"'):
            self.js_click(self.driver, self.locators.AUTO_TYPE_MENU)
            self.element_is_visible(self.locators.AUTO_TYPE).click()
        with allure.step('Заполнение поля "Email"'):
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(data.email)
        with allure.step('Заполнение поля "Сообщение"'):
            self.element_is_present(self.locators.MESSAGE_FIELD).send_keys(data.message)
