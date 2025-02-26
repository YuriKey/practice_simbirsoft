from data.assertions import assertions
from data.urls import urls
import pytest
from locators import main_page_locators as locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from pages.main_page import MainPage
import time

fake = Faker()


@pytest.mark.parametrize("open_page", [urls.URL], indirect=True)
def test_form_fill(driver, open_page):
    page = MainPage(driver)

    """Генерируем имя, пароль, email"""
    name = fake.name()
    password = fake.password()
    email = fake.email()

    """Заполняем имя, пароль, выбираем любимые напитки"""
    page.interact_with_element(driver, locators.name_field_locator, action="send_keys", value=name)
    page.interact_with_element(driver, locators.password_field_locator, action="send_keys", value=password)
    page.interact_with_element(driver, locators.milk_checkbox_locator, action="click")
    page.interact_with_element(driver, locators.coffee_checkbox_locator, action="click")

    """Выбираем любимый цвет"""
    page.js_click(driver, locators.yellow_radiobutton_locator)

    """Раскрываем выпадающий список и выбираем вариант"""
    page.js_click(driver, locators.auto_type_menu_locator)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locators.auto_type_locator)).click()

    """Вводим email"""
    page.interact_with_element(driver, locators.email_field_locator, action="send_keys", value=email)

    """Получаем список инструментов, формируем и вводим сообщение в поле "Message"""
    tools_area = page.interact_with_element(driver, locators.tools_area).split('\n')
    tools_count = len(tools_area)
    largest_tool = sorted(tools_area, key=len)[-1]
    message_text = f"{tools_count}\n{largest_tool}"
    page.interact_with_element(driver, locators.message_field_locator, action="send_keys", value=message_text)
    time.sleep(7)

    """Нажимаем кнопку "Submit"""
    page.interact_with_element(driver, locators.submit_button_locator, action="click")
    time.sleep(2)

    assertions.assert_text_in_alert(driver, "Message received!")

