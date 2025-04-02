from http import HTTPStatus

import allure
import requests

from api_tests.data.data_generator.item_generator import ItemGenerator
from api_tests.data.urls import urls
from api_tests.src.assertions import assertions as a

generator = ItemGenerator()


@allure.epic("Тестирование API.")
@allure.feature("Сущность.")
@allure.testcase("test_04_create_item")
@allure.title("Изменение сущности.")
def test_update_item(create_item):
    with allure.step("Создать сущность. Получить ее id."):
        item_id = create_item[0]
        created_data = create_item[1]

    with allure.step("Сгенерировать данные для изменения."):
        data = generator.generate_item()

    with allure.step("Отправить запрос на изменение сущности."):
        response = requests.patch(f"{urls.BASE_URL}/patch/{item_id}", json=data)

    with allure.step("Проверить статус код запроса на изменение сущности."):
        a.assert_status_code(response, HTTPStatus.NO_CONTENT)

    with allure.step("Проверить, что данные изменились."):
        response_updated = requests.get(f"{urls.BASE_URL}/get/{item_id}")

        a.assert_props(response_updated, data)
        assert response_updated.json()["id"] == item_id
        a.assert_props_not_equal(response_updated, created_data)
