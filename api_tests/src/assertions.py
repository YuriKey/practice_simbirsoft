from requests import Response


class Assertions:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code=200):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, (
            f"Некорректный статус код ответа: ожидается {expected_status_code}, но получен"
            f" {actual_status_code}")

    @staticmethod
    def assert_props(json1, json2):
        assert json1.json()["addition"]["additional_info"] == json2["addition"]["additional_info"]
        assert json1.json()["addition"]["additional_number"] == json2["addition"]["additional_number"]
        assert json1.json()["important_numbers"] == json2["important_numbers"]
        assert json1.json()["title"] == json2["title"]

    @staticmethod
    def assert_props_not_equal(json1, json2):
        assert json1.json()["addition"]["additional_info"] != json2["addition"]["additional_info"]
        assert json1.json()["addition"]["additional_number"] != json2["addition"]["additional_number"]
        assert json1.json()["important_numbers"] != json2["important_numbers"]
        assert json1.json()["title"] != json2["title"]


assertions = Assertions()
