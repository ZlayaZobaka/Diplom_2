import allure
import helpers
import pytest
import requests
from api import Api
from data import ErrorMsg


class TestAuthLogin:

    @allure.title('Тест успешного логина пользователя')
    @allure.description('Успешный запрос логина пользователя возвращает HTTP 200 и токен')
    def test_login_user_correct_data_successful(self, register_user_payload, login_user_payload):
        api = Api()
        api.register_user(register_user_payload)
        response = api.login_user(login_user_payload)

        assert (response.status_code == requests.codes['ok'] and
                str(response.json()['accessToken']).startswith('Bearer'))

    @allure.title('Тест авторизации пользователя с неправильным логином/паролем')
    @allure.description('Если неправильно указать логин или пароль запрос возвращает ошибку Not Found')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_user_incorrect_data_return_unauthorized_error(
            self, register_user_payload, login_user_payload, field):
        api = Api()
        api.register_user(register_user_payload)
        login_user_payload[field] = helpers.generate_random_string()
        response = api.login_user(login_user_payload)

        assert (response.status_code == requests.codes['unauthorized'] and
                response.json()['message'] == ErrorMsg.INCORRECT_PASSWORD)
