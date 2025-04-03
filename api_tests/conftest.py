import allure
import pytest
import requests

from api_tests.data.data_generator.item_generator import ItemGenerator
from api_tests.data.urls import urls

generator = ItemGenerator()


@pytest.fixture(scope="module")
@allure.title("Генерация случайных данных для сущности.")
def create_item():
    data = generator.generate_item()
    response = requests.post(f"{urls.BASE_URL}/create", json=data)
    item_id = response.json()
    return item_id, data
