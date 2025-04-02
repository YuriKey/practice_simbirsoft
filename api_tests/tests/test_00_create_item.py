import allure
import requests

from api_tests.data.data_generator.item_generator import ItemGenerator
from api_tests.data.urls import urls
from api_tests.src.assertions import assertions as a

generator = ItemGenerator()


@allure.epic("Тестирование API.")
@allure.feature("Сущность.")
@allure.testcase("test_00_create_item")
@allure.title("Создание сущности.")
def test_create_item():
    with allure.step("Сгенерировать данные для сущности."):
        data = generator.generate_item()

    with allure.step("Отправить запрос на создание сущности. Получить её id."):
        response = requests.post(f"{urls.BASE_URL}/create", json=data)
        created_item_id = response.json()

    with allure.step("Проверить статус код запроса на создание сущности."):
        a.assert_status_code(response)

    with allure.step("Получить сущность по id."):
        created_item = requests.get(f"{urls.BASE_URL}/get/{created_item_id}")

    with allure.step("Проверить статус код запроса на получение сущности."):
        a.assert_status_code(created_item)

    with allure.step("Сравнить сгенерированные и полученные данные."):
        a.assert_props(created_item, data)
