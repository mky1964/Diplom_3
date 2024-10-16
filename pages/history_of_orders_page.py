
import allure
from locators.history_of_orders_locators import HistoryOfOrderLocators
from pages.base_page import BasePage



class HistoryOfOrdersPage(BasePage):

    @allure.step('find_order_latest_order_number_in_history_of_orders')
    def get_order_latest_order_number_in_history_of_orders(self, delay_time): #Получить номер последнего заказа из истории
        self.find_element_presented(HistoryOfOrderLocators.LATEST_ORDER_NUMBER, delay_time)
        latest_number_order_in_history = self.find_element_presented(HistoryOfOrderLocators.LATEST_ORDER_NUMBER, delay_time).text
        return latest_number_order_in_history


