from faker import Faker


class BaseGenerator:
    def __init__(self):
        self.faker = Faker()

    def get_random_number(self, number):
        if number is None:
            return self.faker.random_number()
        return number

    def get_random_string(self, string):
        if string is None:
            return self.faker.sentence()
        return string
