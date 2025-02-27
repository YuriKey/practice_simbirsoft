from dataclasses import dataclass
from faker import Faker

fake = Faker()


@dataclass
class MainPageData:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    name: str = fake.name()
    password: str = fake.password()
    email: str = fake.email()
    water_checkbox = None
    milk_checkbox = None
    coffee_checkbox = None
    wine_checkbox = None
    ctrl_alt_del_checkbox = None
    favorite_color = None
    message: str = None
