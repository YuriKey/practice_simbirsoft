import pytest
from data.assertions import assertions
from data.urls import urls
import requests
from http import HTTPStatus


@pytest.mark.parametrize("url", [urls.URL])
def test_get_title(driver, url):
    driver.get(url)
    response = requests.get(url)

    assertions.assert_status_code(response, 200)
    assertions.assert_page_title(driver, "Form Fields | Practice Automation")
