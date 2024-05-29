import allure
from faker import Faker
from data import WellKnownConstants


@allure.title('Извлекаем id ингредиентов из ответа')
def get_ingredients_ids(json) -> dict:
    buns = [x['_id'] for x in json if x['type'] == 'bun']
    mains = [x['_id'] for x in json if x['type'] == 'main']
    sauces = [x['_id'] for x in json if x['type'] == 'sauce']
    return {'buns': buns, 'mains': mains, 'sauces': sauces}


@allure.title('Создаем случайную строку')
def generate_random_string(length: int = WellKnownConstants.RANDOM_STRING_LEN) -> str:
    return Faker().text(length)


@allure.title('Создаем случайный email')
def generate_random_mail() -> str:
    return Faker().email(domain=WellKnownConstants.MAIL_DOMAIN)


@allure.title('Создаем случайный рецепт')
def get_recipe(ids: dict, count: int) -> list:
    result = []
    # первым ингредиентом добавляем булку
    if count:
        result.append(ids.get('buns')[Faker().random_int(0, len(ids.get('buns'))) - 1])
        count -= 1
    # вторым соус
    if count:
        result.append(ids.get('sauces')[Faker().random_int(0, len(ids.get('sauces'))) - 1])
        count -= 1
    # последними добавляем начинки
    for _ in range(count):
        result.append(ids.get('mains')[Faker().random_int(0, len(ids.get('mains'))) - 1])

    return result

