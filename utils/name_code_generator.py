from faker import Faker
import random

faker = Faker()


def post_code_generator():
    return ''.join(random.choices('0123456789', k=10))


def first_name_generator(post_code):
    parts = [post_code[i:i + 2] for i in range(0, len(post_code), 2)]

    first_name = ''
    for part in parts:
        num = int(part)
        letter_index = num % 26
        letter = chr(ord('a') + letter_index)
        first_name += letter

    return first_name


def last_name_generator():
    return faker.last_name()
