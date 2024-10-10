import allure
from pages.base_page import BasePage
from locators.constants import Constants
import requests

class ApiPage(BasePage):
    @allure.step('registration_of_new_user')
    def registration_of_new_user(self, new_user):
        #Регистрация нового пользователя. Возвращает dict с email, password, name, accsessToken

        new_user_1 = new_user
        for i in range(1, 100):
            response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user_1, timeout=120)
            if response.status_code != 200:
                pass
            else:
                response_1 = response.json()
                response_2 = response_1.values()
                accessToken = list(response_2)[2]
                new_user_1['token'] = accessToken
                break
        return new_user_1

    @allure.step('deleting_of_new_user')
    def deleting_of_new_user(self, new_user_with_accesstoken):
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']},timeout=30)


    @allure.step('registration_of_new_user')
    def creating_an_order_for_new_user(self, new_user_with_accesstoken):
        token = new_user_with_accesstoken['token']
        order_ingredients = {
            'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                      headers={'Authorization': token}, timeout=30)

    @allure.step('login_account_from_main_page')
    def login_account_by_requests(self, new_user):#Залогинить пользователя из main_page
        result = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', json=new_user, timeout=120)

    @allure.step('set_an_order_api')
    def set_an_order_api(self, new_user_with_token, delay_time):
        for i in range(1, 100):
            token = new_user_with_token['token']
            order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
            response = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                                     headers={'Authorization': token}, timeout=delay_time)
            response_1 = response.json()['order']['number']
            if response.status_code == 200 or response.status_code == 201:
                break
            else:
                pass
        return response_1
