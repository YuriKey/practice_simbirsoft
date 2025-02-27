from data.assertions import assertions
from data.urls import urls
import pytest
from locators.main_page_locators import MainPageLocators
from faker import Faker
from pages.main_page import MainPage
from data.main_page_data import MainPageData

fake = Faker()
locators = MainPageLocators()


@pytest.mark.parametrize("open_page", [urls.URL], indirect=True)
def test_form_fill(driver, open_page):
    page = MainPage(driver)
    data = MainPageData()

    tools_area = page.find_element(locators.TOOLS_AREA).text.split('\n')
    data.message = f"{len(tools_area)}\n{sorted(tools_area, key=len)[-1]}"

    page.fill_form(data)

    page.js_click(driver, locators.SUBMIT_BUTTON)
    assertions.assert_text_in_alert(driver, "Message received!")

