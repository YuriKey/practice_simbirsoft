import allure
import requests

from api_tests.data.data_generator.item_generator import ItemGenerator
from api_tests.data.dataclasses.item_data import ItemData
from api_tests.data.urls import urls
from api_tests.utils.assertions import assertions as a

generator = ItemGenerator()


@allure.epic("Тестирование API.")
@allure.feature("Работа с сущностями.")
@allure.testcase("00_Создание сущности.")
class TestItemCreate:
    @allure.title("Создание и проверка новой сущности.")
    @allure.description("""
        Тест проверяет:
        1. Генерацию данных для сущности.
        2. Создание сущности через API.
        3. Получение созданной сущности.
        4. Идентичность полученных и сгенерированных данных.
        """)
    def test_create_item(self):
        with allure.step("1. Сгенерировать данные для сущности."):
            data = generator.generate_item()

        with allure.step("2. Отправить запрос на создание сущности. Получить её id."):
            response_post = requests.post(f"{urls.BASE_URL}/create", json=data)
            created_item_id = response_post.json()

        with allure.step("3. Проверить статус код запроса на создание сущности."):
            a.assert_status_code(response_post)

        with allure.step("4. Получить сущность по id. Произвести валидацию через Pydantic."):
            response_get = requests.get(f"{urls.BASE_URL}/get/{created_item_id}")
            a.assert_status_code(response_get)
            item = ItemData(**response_get.json())

        with allure.step("5. Сравнить сгенерированные и полученные данные."):
            a.assert_props_are_equal(item, data)
