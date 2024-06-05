import allure
import pytest
import helpers
import copy
from api import Api


@allure.step(f'Создаем запрос на создание пользователя')
@pytest.fixture(scope='function')
def register_user_payload():
    payload = {
        'email': helpers.generate_random_mail(),
        'name': helpers.generate_random_string(),
        'password': helpers.generate_random_string()
    }

    yield payload

    del payload['name']
    api = Api()
    api.login_user(payload)

    del payload['password']
    api.delete_user(payload)


@allure.step(f'Создаем запрос на авторизацию пользователя')
@pytest.fixture(scope='function')
def login_user_payload(register_user_payload):
    payload = copy.copy(register_user_payload)
    del payload['name']
    return payload


@allure.step(f'Получаем список id ингредиентов')
@pytest.fixture(scope='function')
def get_ingredients():
    api = Api()
    response = api.get_ingredients()
    return helpers.get_ingredients_ids(response.json()['data'])
