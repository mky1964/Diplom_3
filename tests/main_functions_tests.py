import time
import requests
from locators.constructor_locators import ConstructorLocators
from locators.constants import Constants
from locators.private_account_locators import PrivateAccountLocators
from locators.order_feed_locators import OrderFeedLocators
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, new_user
from pages.main_page import MainPage
from pages.account_page import Account
from selenium.webdriver.common.by import By

class TestMainFunctions:

    @allure.feature('test_passover_from_pr_acc_to_orders_feed')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Переход из Личного лабинета в Ленту Заказов')
    def test_passover_from_pr_account_to_orders_feed(self, driver, new_user):
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
        account_1.click_on_element_located(PrivateAccountLocators.ORDER_FEED_BUTTON, 5)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            OrderFeedLocators.ORDER_FEED_MAIN_HEADLINE)), f'Заголовок "Вход" не виден'
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})



    @allure.feature('test_passover_from_pr_account_to_constructor')
    @allure.description('Позитивный тест.Проверка основного функционала.'
                        ' Переход из Личного лабинета в Конструктор')
    def test_passover_from_pr_account_to_constructor(self, driver, new_user):
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
        account_1.click_on_element_located(PrivateAccountLocators.CONSTRUCTOR_BUTTON, 5)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            ConstructorLocators.ASSEMBLE_BURGER_HEADLINE)), f'Заголовок "Соберите бургер" не виден'
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})

    @allure.feature('test_in_constructor_get_ingredients_details_by_clicking_ingredient')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' В конструкторе если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_in_constructor_get_ingredients_details_by_clicking_ingredient(self, driver):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        main_page_1.click_on_element_located(ConstructorLocators.CRATER_BUN_ICON, 5)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            ConstructorLocators.INGREDIENT_DETAILS_CRATER_BUN)), f'Заголовок "Детали ингредиента" не виден'

    @allure.feature('test_closing_ingredient_details')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' всплывающее окно  с ингредиентами закрывается кликом по крестику')
    def test_closing_ingredient_details(self, driver):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        main_page_1.click_on_element_located(ConstructorLocators.CRATER_BUN_ICON, 5)
        main_page_1.click_on_element_located(ConstructorLocators.CLOSING_BUTTON_INGREDIENT_DETAILS, 5)
        time.sleep(2)
        assert (main_page_1.check_exists_by_xpath(ConstructorLocators.INGREDIENT_DETAILS_CRATER_BUN) != True),\
            f'Окно с деталями ингредиента не закрывается'

    @allure.feature('test_after_adding_of_ingredient_counter_add_1')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_after_adding_of_ingredient_counter_add_1(self, driver):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        initial_count_num = int(main_page_1.find_element_located(ConstructorLocators.COUNTER_OF_CRATER_BUN, 5).text)
        print(initial_count_num)
        WebDriverWait(driver, 30).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))
        main_page_1.drag_and_drop_element(ConstructorLocators.CRATER_BUN_ICON, ConstructorLocators.ORDER_BUCKET_PLACE, 5)
        time.sleep(10)
        final_count_num = int(main_page_1.find_element_located(ConstructorLocators.COUNTER_OF_CRATER_BUN, 20).text)
        delta = final_count_num - initial_count_num
        assert delta == 2, f'Счетчик ингредиента не работает'

    @allure.feature('test_passover_from_pr_account_to_constructor')
    @allure.description('Позитивный тест.Проверка основного функционала.'
                        ' залогиненный пользователь может оформить заказ')
    def test_user_logins_and_places_an_order(self, driver, new_user):
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
        WebDriverWait(driver, 20).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))
        main_page_1.drag_and_drop_element(ConstructorLocators.CRATER_BUN_ICON, ConstructorLocators.ORDER_BUCKET_PLACE, 20)
        WebDriverWait(driver, 20).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))
        main_page_1.click_on_element_located(ConstructorLocators.PLACE_ORDER_BUTTON, 5)
        time.sleep(10)
        order_number = int(main_page_1.find_element_located(ConstructorLocators.ORDER_NUMBER_COUNTER_IN_WINDOW, 5).text)
        print(order_number)

        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            ConstructorLocators.ID_ORDER_HEADER)) and (order_number != 9999), f'Идентификатор заказа" не виден на всплывающем окне'
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})



