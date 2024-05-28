import allure
import helpers
import pytest
import requests


class TestAuthLogin:

    @allure.title('Тест успешного изменения данных пользователя')
    @allure.description('Запрос изменения данных пользователя с авторизацией возвращает {"success":true}')
    @pytest.mark.parametrize('field,value',
                             [
                                 ['email', helpers.generate_random_mail()],
                                 ['name', helpers.generate_random_string()],
                                 ['password', helpers.generate_random_string()]
                             ])
    def test_change_user_correct_data_successful(
            self, api, register_user_payload, delete_user, field, value):
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
    def test_change_user_correct_data_successful(
            self, api, register_user_payload, delete_user, field, value):
        api.register_user(register_user_payload)

        response = api.change_user({field: value}, use_auth_token=False)

        assert (response.status_code == requests.codes['unauthorized'] and
                response.json()['message'] == 'You should be authorised')

