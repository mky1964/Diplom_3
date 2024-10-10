import time
import allure
from selenium.webdriver.common.by import By
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage



class OrderFeedPage(BasePage):

    @allure.step('click_on_the_first_order_card_in_order_feed')
    def click_on_the_first_order_card_in_order_feed(self, delay_time):  #Кликнуть переход "Вход в Аккаунт"
        self.click_on_element_located(OrderFeedLocators.ORDER_IN_ORDER_FEED_NUM_1, delay_time)


    @allure.step('get_number_in_order_feed_by_order_number_from_history')
    def find_number_in_order_feed_by_order_number_from_history(self, number_order_in_history): #Найти заказ в ленте по номеру последнего заказа из истории
        num = ''
        for i in range(1, 50):
            num = self.find_element_presented((By.XPATH, f'//li[{i}][@class="OrderHistory_listItem__2x95r mb-6"]'), 5).text
            if number_order_in_history in num:
                result = True
                break
            else:
                pass
        return num #Номер карточки в ленте заказов

    @allure.step('get_number_of_orders_all_time_in_order_feed')
    def get_number_of_orders_all_time_in_order_feed(self, delay_time):  #Получить количество заказов за всё время из Ленты заказов
        number_of_orders_all_time = int(
            self.find_element_presented(OrderFeedLocators.ORDER_NUMBER_ALL_TIME, delay_time).text)
        return number_of_orders_all_time

    @allure.step('get_number_of_orders_today_in_order_feed')
    def get_number_of_orders_today_in_order_feed(self, delay_time):  #Получить количество заказов за сегодня из Ленты заказов
        number_of_orders_today = int(
            self.find_element_presented(OrderFeedLocators.ORDER_NUMBER_TODAY, delay_time).text)
        return number_of_orders_today

    @allure.step('get_orders_number_in_work_in_order_feed_actual')
    def get_orders_number_in_work_in_order_feed_actual(self, delay_time):  #Получить номер заказа в работе в Ленте заказов

        order_number_in_work_actual = self.find_element_presented(OrderFeedLocators.ORDER_NUMBER_IN_WORK, delay_time).text
        number = order_number_in_work_actual
        return str(number)

    @allure.step('get_orders_number_in_work_in_order_feed_actual')
    def get_orders_number_in_work_in_order_feed_expected(self, response_api):  # Получить номер заказа в работе в Ленте заказов поответу API

        number = response_api
        order_number_in_work_expected = f'0{number}'
        return order_number_in_work_expected

    @allure.step('checking_of_presence_of_order_details_card_number')
    def checking_of_presence_of_order_details_card_number(self, delay_time):
        result = self.find_element_presented(OrderFeedLocators.ORDER_DETAIL_CARD_NUMBER, delay_time)
        return result

    @allure.step('checking_of_presence_of_order_feed_main_headline')
    def checking_of_presence_of_order_feed_main_headline(self, delay_time):
        result = self.find_element_presented(OrderFeedLocators.ORDER_FEED_MAIN_HEADLINE, delay_time)
        return result

    @allure.step('checking_of_presence_of_order_feed_main_headline')
    def checking_of_presence_assemble_burger_in_constructor(self, delay_time):
        result = self.find_element_presented(OrderFeedLocators.ASSEMBLE_BURGER_HEADLINE, delay_time)
        return result




