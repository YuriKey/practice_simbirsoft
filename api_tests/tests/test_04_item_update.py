from http import HTTPStatus

import allure
import requests

from api_tests.data.data_generator.item_generator import ItemGenerator
from api_tests.data.dataclasses.item_data import ItemData
from api_tests.data.urls import urls
from api_tests.utils.assertions import assertions as a

generator = ItemGenerator()


@allure.epic("Тестирование API.")
@allure.feature("Работа с сущностями.")
@allure.testcase("04_Изменение сущности.")
@allure.title("Изменение сущности.")
class TestItemUpdate:
    @allure.title("Изменение сущности (positive case).")
    @allure.description("""
    Тест проверяет:
    1. Получение данных сущности по ID.
    2. Корректность PATCH-запроса для обновления сущности.
    3. Идентичность данных измененной сущности переданным данными.
    4. Изменение полей сущности кроме ID.
    """)
    def test_update_item(self, create_item):
        with allure.step("1. Получить тестовые данные из фикстуры."):
            item_id, original_data = create_item
            original_item = ItemData(**original_data)

        with allure.step("2. Сгенерировать новые данные для обновления."):
            update_data = generator.generate_item()
            ItemData(**update_data)

        with allure.step("3. Отправить PATCH-запрос на обновление."):
            response_patch = requests.patch(f"{urls.BASE_URL}/patch/{item_id}", json=update_data)
            a.assert_status_code(response_patch, HTTPStatus.NO_CONTENT)

        with allure.step("4. Получить обновленную сущность и проверить изменения."):
            response_updated = requests.get(f"{urls.BASE_URL}/get/{item_id}")
            a.assert_status_code(response_updated)

            updated_item = ItemData(**response_updated.json())

            assert updated_item.id == item_id, "ID сущности изменился после обновления."
            a.assert_props_are_equal(updated_item, update_data)
            assert updated_item != original_item, "Данные сущности не изменились после обновления."
