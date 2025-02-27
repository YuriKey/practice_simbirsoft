import pytest
from data.assertions import assertions
from data.urls import urls
import requests
import allure


@allure.title("Проверка заголовка страницы и кода ответа сервера")
@pytest.mark.parametrize("url", [urls.URL])
def test_get_title(driver, url):
    driver.get(url)
    response = requests.get(url)

    with allure.step("Проверка кода ответа сервера"):
        assertions.assert_status_code(response, 200)
    with allure.step("Проверка заголовка страницы"):
        assertions.assert_page_title(driver, "Form Fields | Practice Automation")
