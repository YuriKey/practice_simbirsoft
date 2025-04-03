from typing import Optional, List, Dict, Any

from faker import Faker

from api_tests.data.data_generator.base_generator import BaseGenerator
from api_tests.data.dataclasses.item_data import Addition, ItemData

fake = Faker()


class ItemGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.numbers_count = fake.random_int(2, 5)

    @staticmethod
    def generate_addition(
            additional_info: Optional[str] = None,
            additional_number: Optional[int] = None):
        """Генерация объекта addition."""
        return Addition(
            additional_info=additional_info or fake.sentence(),
            additional_number=additional_number or fake.random_int()
        )

    def generate_important_numbers(
            self,
            numbers: Optional[List[int]] = None,
            count: Optional[int] = None
    ):
        """Генерация списка чисел."""
        if numbers is not None:
            return numbers
        return [fake.random_int() for _ in range(count or self.numbers_count)]

    def generate_item(
            self,
            addition: Optional[Dict[str, Any]] = None,
            important_numbers: Optional[List[int]] = None,
            title: Optional[str] = None,
            verified: bool = True
    ):
        """Основной метод генерации тестовых данных."""
        item = ItemData(
            addition=self.generate_addition(
                additional_info=addition.get("additional_info") if addition else None,
                additional_number=addition.get("additional_number") if addition else None
            ) if addition or True else None,
            important_numbers=self.generate_important_numbers(important_numbers),
            title=self.get_random_string(title),
            verified=verified
        )

        return item.model_dump()
