import time

import allure
import requests
from selenium.webdriver.common.by import By
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage
from pages.account_page import Account


class OrderFeedPage(BasePage):

    @allure.step('click_on_the_first_order_card_in_order_feed')
    def click_on_the_first_order_card_in_order_feed(self, delay_time):  #Кликнуть переход "Вход в Аккаунт"
        time.sleep(3)
        self.click_on_element_located(OrderFeedLocators.ORDER_IN_ORDER_FEED_NUM_1, delay_time)


    @allure.step('get_number_in_order_feed_by_order_number_from_history')
    def find_number_in_order_feed_by_order_number_from_history(self, number_order_in_history): #Найти заказ в ленте по номеру последнего заказа из истории
        time.sleep(3)
        num = ''
        for i in range(1, 50):
            num = self.find_element_presented((By.XPATH, f'//li[{i}][@class="OrderHistory_listItem__2x95r mb-6"]'), 2).text
            if number_order_in_history in num:
                result = True
                break
            else:
                pass
        return num #Номер карточки в ленте заказов

    @allure.step('get_number_of_orders_all_time_in_order_feed')
    def get_number_of_orders_all_time_in_order_feed(self, delay_time):  #Получить количество заказов за всё время из Ленты заказов
        time.sleep(5)
        number_of_orders_all_time = int(
            self.find_element_presented(OrderFeedLocators.ORDER_NUMBER_ALL_TIME, delay_time).text)
        return number_of_orders_all_time

    @allure.step('get_number_of_orders_today_in_order_feed')
    def get_number_of_orders_today_in_order_feed(self, delay_time):  #Получить количество заказов за сегодня из Ленты заказов
        time.sleep(7)
        number_of_orders_today = int(
            self.find_element_presented(OrderFeedLocators.ORDER_NUMBER_TODAY, delay_time).text)
        return number_of_orders_today

    @allure.step('get_orders_number_in_work_in_order_feed_actual')
    def get_orders_number_in_work_in_order_feed_actual(self, delay_time):  #Получить номер заказа в работе в Ленте заказов
        time.sleep(5)
        order_number_in_work_actual = self.find_element_presented(OrderFeedLocators.ORDER_NUMBER_IN_WORK, delay_time).text
        return order_number_in_work_actual

    @allure.step('get_orders_number_in_work_in_order_feed_actual')
    def get_orders_number_in_work_in_order_feed_expected(self, response_api):  # Получить номер заказа в работе в Ленте заказов поответу API
        number = list(response_api.json().values())[-1]['number']
        order_number_in_work_expected = f'0{number}'
        return order_number_in_work_expected
