import time

import allure
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constants import Constants
from locators.constructor_locators import ConstructorLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('click_on_enter_account_button')
    def click_on_enter_account_button(self, delay_time):  #Кликнуть переход "Вход в Аккаунт"
        time.sleep(2)
        self.click_on_element_located(MainPageLocators.ENTER_ACCOUNT_BUTTON, delay_time)

    @allure.step('click_on_enter_account_button')
    def click_on_order_feed_from_main_page(self, delay_time):  #Кликнуть переход "Лента заказов"
        time.sleep(2)
        self.click_on_element_located(MainPageLocators.ORDERS_FEED_FROM_MAIN_BUTTON, delay_time)

    def click_on_set_order_button(self, delay_time):  #Кликнуть переход "Оформить заказ"
        self.click_on_element_located(ConstructorLocators.PLACE_ORDER_BUTTON, 60)
    @allure.step('click_on_crater_bun_button')
    def click_on_crater_bun_button(self, delay_time):  #Кликнуть по кратерной булке
        time.sleep(3)
        self.click_on_element_located(ConstructorLocators.CRATER_BUN_ICON, delay_time)

    @allure.step('click_on_close_button_on_ingredient_detail')
    def click_on_close_button_on_ingredient_detail(self, delay_time):  #Кликнуть по крестику на окне с ингредиентами
        time.sleep(1)
        self.click_on_element_located(ConstructorLocators.CLOSING_BUTTON_INGREDIENT_DETAILS, delay_time)
        time.sleep(1)

    @allure.step('click_on_close_button_on_ingredient_detail')
    def wait_of_vanishing_of_overlay(self, driver, delay_time):  #Ожидание пропадания всплывающего объекта
        time.sleep(1)
        WebDriverWait(driver, delay_time).until_not(EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))

    @allure.step('get_count_number_of_crater_bun_in_constructor')
    def get_count_number_of_crater_bun_in_constructor(self, delay_time):  # Получение значения счетчика Краторной булки
        time.sleep(1)
        count_number =int(self.find_element_located(ConstructorLocators.COUNTER_OF_CRATER_BUN, delay_time).text)
        time.sleep(2)
        return count_number

    @allure.step('get_number_of_new_order_from_window')
    def get_number_of_new_order_from_window(self, delay_time):  # Получение значения счетчика Краторной булки
        time.sleep(1)
        number =int(self.find_element_located(ConstructorLocators.ORDER_NUMBER_COUNTER_IN_WINDOW, 8).text)
        time.sleep(2)
        return number

    @allure.step('drag_and_drop_crater_bun')
    def drag_and_drop_crater_bun(self, delay_time):  # Перетащить краторную булку в корзину
        time.sleep(3)
        self.drag_and_drop_element(ConstructorLocators.CRATER_BUN_ICON, ConstructorLocators.ORDER_BUCKET_PLACE,
                                delay_time)

    @allure.step('click_on_enter_account_button')
    def find_enter_account_button(self, delay_time):  #Найти переход "Вход в Аккаунт"
        self.find_element_located(MainPageLocators.ENTER_ACCOUNT_BUTTON, delay_time)

    @allure.step('click_on_private_account_button')
    def click_on_private_account_button_main_page(self, delay_time):  #Кликнуть переход  на "Личный Кабинет"
        time.sleep(3)
        self.click_on_element_located(MainPageLocators.PRIVATE_ACCOUNT_BUTTON, delay_time)
    @allure.step('set_an_order_ui')
    def set_an_order_ui(self,driver, delay_time):
        WebDriverWait(driver, 20).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))
        time.sleep(2)
        self.drag_and_drop_element(ConstructorLocators.CRATER_BUN_ICON, ConstructorLocators.ORDER_BUCKET_PLACE, delay_time)
        WebDriverWait(driver, 20).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))
        time.sleep(2)
        self.click_on_element_located(ConstructorLocators.PLACE_ORDER_BUTTON, delay_time)
        time.sleep(2)

    @allure.step('close_card_with_new_order')
    def close_card_with_new_order(self, driver, delay_time):
        self.click_on_element_located(ConstructorLocators.CLOSING_ORDER_CARD_BUTTON, delay_time)

    @allure.step('set_an_order_api')
    def set_an_order_api(self, new_user_with_token, delay_time):
        for i in range(1, 100):
            token = new_user_with_token['token']
            order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
            response = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients, headers={'Authorization': token},timeout= delay_time)
            if response.status_code == 200 or response.status_code == 201:
                break
            else:
                pass
            return response

