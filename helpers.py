from faker import Faker
from data import WellKnownConstants


def get_ingredients_ids(json):
    return [x['_id'] for x in json]


def generate_random_string(length=WellKnownConstants.RANDOM_STRING_LEN):
    return Faker().text(length)


def generate_random_mail():
    return Faker().email()


