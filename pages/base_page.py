class BasePage:
    def __init__(self, driver):
        self.urls = None
        self.driver = driver

    def open(self):
        self.driver.get(self.urls.URL)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text
