from data.assertions import assertions
from data.urls import urls
import pytest
from locators.main_page_locators import MainPageLocators
from faker import Faker
from pages.main_page import MainPage
from data.main_page_data import MainPageData
import allure

fake = Faker()
locators = MainPageLocators()


@allure.title("Проверка заполнения формы и текста алерта")
@pytest.mark.parametrize("open_page", [urls.URL], indirect=True)
def test_form_fill(driver, open_page):
    page = MainPage(driver)
    data = MainPageData()

    tools_area = page.find_element(locators.TOOLS_AREA).text.split('\n')
    data.message = f"{len(tools_area)}\n{sorted(tools_area, key=len)[-1]}"

    page.fill_form(data)

    with allure.step("Нажатие кнопки Submit"):
        page.js_click(driver, locators.SUBMIT_BUTTON)

    with allure.step("Прверка текста алерта"):
        assertions.assert_text_in_alert(driver, "Message received!")

