import allure
import helpers
import pytest
import requests
from api import Api
from data import WellKnownConstants, ErrorMsg


class TestOrders:

    @allure.title('Тест успешного создания заказа (с авторизацией)')
    @allure.description('Успешный запрос создания заказа возвращает HTTP 200 и информацию о заказчике')
    @pytest.mark.parametrize('count', [1, 3, 5])
    def test_create_order_with_authorization_successful(
            self, register_user_payload, get_ingredients, count):
        api = Api()
        api.register_user(register_user_payload)
        ids = helpers.get_recipe(get_ingredients, count)
        response = api.create_order({'ingredients': ids})

        assert (response.status_code == requests.codes['ok'] and
                response.json()['success'] is True and
                response.json()['order']['owner']['email'] == register_user_payload['email'])

    @allure.title('Тест успешного создания заказа (без авторизации)')
    @allure.description('Успешный запрос создания заказа возвращает HTTP 200 и "success": true')
    @pytest.mark.parametrize('count', [1, 3, 5])
    def test_create_order_without_authorization_successful(self, get_ingredients, count):
        ids = helpers.get_recipe(get_ingredients, count)
        response = Api().create_order({'ingredients': ids})

        assert (response.status_code == requests.codes['ok'] and
                response.json()['success'] is True)

    @allure.title('Тест попытки создания заказа без ингредиентов')
    @allure.description('Запрос создания заказа без ингредиентов возвращает ошибку Bad Request')
    def test_create_order_without_ingredients_return_bad_request_error(
            self, register_user_payload, get_ingredients):
        api = Api()
        api.register_user(register_user_payload)
        response = api.create_order({'ingredients': []})

        assert (response.status_code == requests.codes['bad_request'] and
                response.json()['message'] == ErrorMsg.EMPTY_INGREDIENT_LIST)

    @allure.title('Тест попытки создания заказа в котором один из ингредиентов с неверным id')
    @allure.description('Запрос создания заказа с неверным id ингредиента возвращает ошибку Bad Request')
    @pytest.mark.parametrize('count', [1, 3])
    def test_create_order_bad_ingredient_id_return_bad_request_error(
            self, register_user_payload, get_ingredients, count):
        api = Api()
        api.register_user(register_user_payload)
        ids = helpers.get_recipe(get_ingredients, count)
        ids[0] = WellKnownConstants.UNKNOWN_ID
        response = api.create_order({'ingredients': ids})

        assert (response.status_code == requests.codes['bad_request'] and
                response.json()['message'] == ErrorMsg.UNKNOWN_INGREDIENT_ID)

    @allure.title('Тест попытки получения списка заказов пользователя (без авторизации)')
    @allure.description('Запрос получения списка заказов пользователя без авторизации возвращает ошибку Unauthorized')
    def test_get_user_orders_without_authorization_return_unauthorized_error(self, get_ingredients):
        ids = helpers.get_recipe(get_ingredients, 1)
        api = Api()
        api.create_order({'ingredients': ids})
        response = api.get_user_orders()

        assert (response.status_code == requests.codes['unauthorized'] and
                response.json()['message'] == ErrorMsg.UNAUTHORIZED_USER)

    @allure.title('Тест успешного получения списка заказов пользователя (с авторизацией)')
    @allure.description('Успешный запрос создания заказа возвращает HTTP 200 и "success": true')
    def test_get_user_orders_with_authorization_successful(self, register_user_payload, get_ingredients):
        api = Api()
        api.register_user(register_user_payload)
        ids = helpers.get_recipe(get_ingredients, 1)
        create_order_response = api.create_order({'ingredients': ids})
        get_order_response = api.get_user_orders()

        assert (get_order_response.status_code == requests.codes['ok'] and
                create_order_response.json()['order']['number'] == get_order_response.json()['orders'][0]['number'])
