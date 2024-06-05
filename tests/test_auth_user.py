import allure
import helpers
import pytest
import requests
from api import Api
from data import ErrorMsg


class TestAuthLogin:

    @allure.title('Тест успешного изменения данных пользователя')
    @allure.description('Запрос изменения данных пользователя с авторизацией возвращает {"success":true}')
    @pytest.mark.parametrize('field,value',
                             [
                                 ['email', helpers.generate_random_mail()],
                                 ['name', helpers.generate_random_string()],
                                 ['password', helpers.generate_random_string()]
                             ])
    def test_change_user_correct_data_successful(self, register_user_payload, field, value):
        api = Api()
        api.register_user(register_user_payload)

        response = api.change_user({field: value})

        assert (response.status_code == requests.codes['ok'] and
                response.json()['success'] is True)

    @allure.title('Тест изменения данных пользователя без авторизации')
    @allure.description('Запрос изменения данных пользователя без авторизации возвращает ошибку Unauthorized')
    @pytest.mark.parametrize('field,value',
                             [
                                 ['email', helpers.generate_random_mail()],
                                 ['name', helpers.generate_random_string()],
                                 ['password', helpers.generate_random_string()]
                             ])
    def test_change_user_without_authorization_return_unauthorized_error(
            self, register_user_payload, field, value):
        Api().register_user(register_user_payload)

        response = Api().change_user({field: value})

        assert (response.status_code == requests.codes['unauthorized'] and
                response.json()['message'] == ErrorMsg.UNAUTHORIZED_USER)

