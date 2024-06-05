import allure
import requests
import json
from data import Url


class Api:

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    @allure.step('Сохраняем accessToken-токен')
    def set_token(self, token):
        self.headers['Authorization'] = token

    @allure.step('Отправляем запрос на создание пользователя')
    def register_user(self, payload):
        response = requests.post(
            url=Url.BASE_URL + Url.AUTH_REGISTER_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

        self.set_token(response.json().get('accessToken'))

        return response

    @allure.step('Отправляем запрос на авторизацию пользователя')
    def login_user(self, payload):
        response = requests.post(
            url=Url.BASE_URL + Url.AUTH_LOGIN_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

        self.set_token(response.json().get('accessToken'))

        return response

    @allure.step('Отправляем запрос на получение данных пользователя')
    def get_user(self):
        response = requests.get(
            url=Url.BASE_URL + Url.AUTH_USER_ENDPOINT,
            headers=self.headers)

        return response

    @allure.step('Отправляем запрос на изменение данных пользователя')
    def change_user(self, payload):
        response = requests.patch(
            url=Url.BASE_URL + Url.AUTH_USER_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

        return response

    @allure.step('Отправляем запрос на удаление пользователя')
    def delete_user(self, payload):
        response = requests.delete(
            url=Url.BASE_URL + Url.AUTH_USER_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

        return response

    @allure.step('Отправляем запрос на получение данных об ингредиентах')
    def get_ingredients(self):
        response = requests.get(
            url=Url.BASE_URL + Url.INGREDIENTS_ENDPOINT,
            headers=self.headers)

        return response

    @allure.step('Отправляем запрос на создание заказа')
    def create_order(self, payload):
        response = requests.post(
            url=Url.BASE_URL + Url.ORDERS_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

        return response

    @allure.step('Отправляем запрос на получение заказов пользователя')
    def get_user_orders(self):
        response = requests.get(
            url=Url.BASE_URL + Url.ORDERS_ENDPOINT,
            headers=self.headers)

        return response
