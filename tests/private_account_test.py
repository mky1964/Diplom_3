import time

import requests
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, new_user
from pages.main_page import MainPage
from pages.account_page import Account
from locators.constants import Constants
from locators.private_account_locators import PrivateAccountLocators



class TestPrivateAccount:

    @allure.feature('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь переходит по клику на «Личный кабинет» на страницу авторизации Личного лабинета.'
                        ' Авторизируется. Опять переходит в личный кабинет. Обнаруживается кгнопка "История заказов". Пользователь авторизирован')
    def test_passover_via_pr_acc_button_to_pr_acc(self, driver,new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        print(new_user_with_accesstoken)
        main_page_1.click_on_private_account_button(5)
        time.sleep(3)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER, new_user_with_accesstoken['email'],5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER, new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)
        main_page_1.click_on_private_account_button(10)
        time.sleep(3)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            PrivateAccountLocators.ORDERS_HISTORY_BUTTON)), f'Заголовок "История заказов" не виден'
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})


    @allure.feature('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь переходит по кнопке "История Заказов"')
    def test_passover_via_pr_acc_to_orders_history(self, driver,new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        user = new_user
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        print(new_user_with_accesstoken)
        order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        time.sleep(5)
        accessToken_1 = new_user_with_accesstoken['token']
        requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients, headers={'Authorization': new_user_with_accesstoken['token']})
        main_page_1.click_on_private_account_button(5)
        time.sleep(3)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER, new_user_with_accesstoken['email'],5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER, new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)
        main_page_1.click_on_private_account_button(10)
        time.sleep(3)
        main_page_1.click_on_element_located(PrivateAccountLocators.ORDERS_HISTORY_BUTTON, 5)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            PrivateAccountLocators.ORDER_WINDOW)), f'Заказов нет'
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})

    @allure.feature('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь выходит их Личного Кабинета по кнопке "Выход"')
    def test_exit_from_account(self, driver,new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        user = new_user
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        print(new_user_with_accesstoken)
        order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response_1 = requests.post(Constants.REGISTRATION_USER_URL, json=user)
        time.sleep(5)
        accessToken_1 = new_user_with_accesstoken['token']
        time.sleep(3)
        main_page_1.click_on_private_account_button(5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER, new_user_with_accesstoken['email'],5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER, new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)
        main_page_1.click_on_private_account_button(10)
        time.sleep(3)
        main_page_1.click_on_element_located(PrivateAccountLocators.EXIT_BUTTON_FROM_ACCOUNT, 5)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            PrivateAccountLocators.ENTER_BUTTON)), f' хедера "Войти" нет'
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})
