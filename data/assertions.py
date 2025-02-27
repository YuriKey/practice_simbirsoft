from requests import Response
from colorama import Fore, Back, Style, init

init()


class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, (
            f'{Fore.MAGENTA}Expected status code "{expected_status_code}", '
            f'but got "{actual_status_code}".{Style.RESET_ALL}')
        print(f'{Fore.GREEN}\nActual status code: "{actual_status_code}".'
              f'\nExpected status code: {expected_status_code}".{Style.RESET_ALL}')

    @staticmethod
    def assert_page_title(driver, expected_title: str):
        actual_title = driver.title
        assert actual_title == expected_title, \
            (f'{Fore.MAGENTA}Expected title "{expected_title}", '
             f'but got "{actual_title}".{Style.RESET_ALL}')
        print(f'{Fore.GREEN}\nActual title: "{actual_title}".'
              f'\nExpected title: "{expected_title}".{Style.RESET_ALL}')

    @staticmethod
    def assert_text_in_alert(driver, expected_alert_text: str):
        alert = driver.switch_to.alert
        actual_alert_text = alert.text
        assert actual_alert_text == expected_alert_text, (
            f'{Fore.MAGENTA}Expected alert text "{expected_alert_text}", '
            f'but got "{actual_alert_text}".{Style.RESET_ALL}')
        print(f'{Fore.GREEN}\nActual alert text: "{actual_alert_text}".'
              f'\nExpected alert text: "{expected_alert_text}".{Style.RESET_ALL}')


assertions = Assertions()
