from requests import Response


class Assertions:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code=200):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, (
            f"Некорректный статус код ответа: ожидается {expected_status_code}, но получен"
            f" {actual_status_code}")

    @staticmethod
    def assert_props_are_equal(item_dict, expected_data):
        actual_data = item_dict.model_dump()

        assert actual_data["title"] == expected_data["title"], "Поле title не совпадает."
        assert actual_data["important_numbers"] == expected_data["important_numbers"], \
            "Поле important_numbers не совпадает."
        assert actual_data["addition"]["additional_info"] == expected_data["addition"]["additional_info"], \
            "Поле additional_info не совпадает."
        assert actual_data["addition"]["additional_number"] == expected_data["addition"]["additional_number"], \
            "Поле additional_number не совпадает."

    @staticmethod
    def assert_props_not_equal(item_dict, expected_data):
        actual_data = item_dict.model_dump()

        assert actual_data["title"] != expected_data["title"], \
            "Поле title не изменилось"
        assert actual_data["important_numbers"] != expected_data["important_numbers"], \
            "Поле important_numbers не изменилось"
        assert actual_data["addition"]["additional_info"] != expected_data["addition"]["additional_info"], \
            "Поле additional_info не изменился"
        assert actual_data["addition"]["additional_number"] != expected_data["addition"]["additional_number"], \
            "Поле additional_number не изменился"


assertions = Assertions()
