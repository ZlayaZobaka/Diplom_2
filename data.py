class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    INGREDIENTS_ENDPOINT = '/ingredients'
    AUTH_REGISTER_ENDPOINT = '/auth/register'
    AUTH_LOGIN_ENDPOINT = '/auth/login'
    AUTH_USER_ENDPOINT = '/auth/user'
    ORDERS_ENDPOINT = '/orders'


class WellKnownConstants:
    RANDOM_STRING_LEN = 5
    MAIL_DOMAIN = "mytests.com"
    ID_LEN = 24
    UNKNOWN_ID = '00c0c5a71d1f82001bdaaa70'

class ErrorMsg:
    EMPTY_INGREDIENT_LIST = 'Ingredient ids must be provided'
    UNKNOWN_INGREDIENT_ID = 'One or more ids provided are incorrect'
    UNAUTHORIZED_USER = 'You should be authorised'
    INCORRECT_PASSWORD = 'email or password are incorrect'
    USER_ALREADY_EXISTS = 'User already exists'
    REQUIRED_FIELDS_ARE_NOT_FILLED = 'Email, password and name are required fields'

