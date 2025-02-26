from requests import Response


class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, (
            f'Expected status code "{expected_status_code}", but got "{actual_status_code}"')

    @staticmethod
    def assert_page_title(driver, expected_title: str):
        actual_title = driver.title
        assert actual_title == expected_title, \
            f'Expected title "{expected_title}", but got "{actual_title}"'

    @staticmethod
    def assert_text_in_alert(driver, expected_alert_text: str):
        alert = driver.switch_to.alert
        actual_alert_text = alert.text
        assert actual_alert_text == expected_alert_text, (
            f'Expected alert text "{expected_alert_text}", but got "{actual_alert_text}"'
        )


assertions = Assertions()
