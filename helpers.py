from faker import Faker
from data import WellKnownConstants


def get_ingredients_ids(json):
    return [x['_id'] for x in json]


def generate_random_string(length=WellKnownConstants.RANDOM_STRING_LEN):
    return Faker().text(length)


def generate_random_mail():
    return Faker().email(domain=WellKnownConstants.MAIL_DOMAIN)


def get_recipe(ids: list, count: int):
    result = []
    for _ in range(count):
        result.append(ids[Faker().random_int(0, len(ids)) - 1])
    return result

