import allure
import requests

from api_tests.data.urls import urls
from api_tests.src.assertions import assertions as a


@allure.epic("Тестирование API.")
@allure.feature("Сущность.")
@allure.testcase("test_03_get_all_items")
@allure.title("Получение всех сущностей.")
def test_get_all_items(create_item):
    with allure.step("Создать сущность. Отправить запрос на получение всех "
                     "сущностей первой страницы при perPage=5."):
        response = requests.get(f"{urls.BASE_URL}/getAll/?page=1&perPage=5")
        items_list = response.json()["entity"]

    with allure.step("Проверить статус код запроса на получение всех сущностей."):
        a.assert_status_code(response)

    with allure.step("Проверить. что количество сущностей в ответе не менее 1 и не более 5."):
        assert 1 <= len(items_list) <= 5, (f"Количество сущностей в ответе не равно ожидаемому"
                                           f". Ожидаемое: 1-5. Фактическое: {len(items_list)}")
