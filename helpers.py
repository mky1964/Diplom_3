import allure
from faker import Faker
from data.data import Data
import requests
from constants.constants import Constants

@allure.step('new_user_helper')
def new_user_helper():

    faker_1 = Faker()
    # генерируем логин, пароль и имя курьера
    email = faker_1.email()
    password = faker_1.password(10)
    name = faker_1.name()
    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    # возвращаем список
    return payload

@allure.step('new_user_helper')
def set_order_helper(new_user_with_token, delay_time):
    for i in range(1, 100):
        token = new_user_with_token['token']
        order_ingredients = {'ingredients': [Data.HASH_INGREDIENT_FLUO_BUN, Data.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                                 headers={'Authorization': token}, timeout=delay_time)
        response_1 = response.json()['order']['number']
        if response.status_code == 200 or response.status_code == 201:
            break
        else:
            pass
    return response_1



