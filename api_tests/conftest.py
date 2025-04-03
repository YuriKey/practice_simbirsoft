import allure
import pytest
import requests

from api_tests.data.data_generator.item_generator import ItemGenerator
from api_tests.data.urls import urls

generator = ItemGenerator()


@pytest.fixture(scope="module")
def create_item():
    data = generator.generate_item()
    response = requests.post(f"{urls.BASE_URL}/create", json=data)
    item_id = response.json()
    with allure.step("Сгенерированы случайные данные для сущности."):
        return item_id, data
