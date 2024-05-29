import allure
import pytest
import requests
from data import ErrorMsg


class TestAuthRegister:

    @allure.title('Тест успешного создания пользователя')
    @allure.description('Успешный запрос создания пользователя возвращает HTTP 200 и токен')
    def test_register_user_correct_data_successful(self, api, register_user_payload, delete_user):
        response = api.register_user(register_user_payload)

        assert (response.status_code == requests.codes['ok'] and
                str(response.json()['accessToken']).startswith('Bearer'))

    @allure.title('Тест создания пользователя с логином, который уже зарегистрирован')
    @allure.description('Если создать пользователя с логином, который уже есть, возвращается ошибка Сonflict')
    def test_register_user_same_mail_return_conflict_error(self, api, register_user_payload, delete_user):
        api.register_user(register_user_payload)
        response = api.register_user(register_user_payload)

        assert (response.status_code == requests.codes['forbidden'] and
               response.json()['message'] == ErrorMsg.USER_ALREADY_EXISTS)

    @allure.title('Тест создания пользователя, если отсутствует часть обязательных полей')
    @allure.description('Если одного из полей нет, запрос возвращает ошибку Bad Request')
    @pytest.mark.parametrize('field', ['email', 'name', 'password'])
    def test_register_user_empty_data_return_bad_request_error(self, api, register_user_payload, delete_user, field):
        with allure.step(f'Очищаем поле {field}'):
            register_user_payload[field] = ''
            response = api.register_user(register_user_payload)

        assert (response.status_code == requests.codes['forbidden'] and
                response.json()['message'] == ErrorMsg.REQUIRED_FIELDS_ARE_NOT_FILLED)
