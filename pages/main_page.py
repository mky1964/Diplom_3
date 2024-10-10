import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constants import Constants
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('click_on_enter_account_button')
    def click_on_enter_account_button(self, delay_time):  #Кликнуть переход "Вход в Аккаунт"
        self.click_on_element_located(MainPageLocators.ENTER_ACCOUNT_BUTTON, delay_time)

    @allure.step('click_on_enter_account_button')
    def click_on_order_feed_from_main_page(self, delay_time):  #Кликнуть переход "Лента заказов"
        self.wait_of_vanishing_of_overlay_base(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE,60)
        self.click_on_element_located(MainPageLocators.ORDERS_FEED_FROM_MAIN_BUTTON, delay_time)

    def click_on_set_order_button(self, delay_time):  #Кликнуть переход "Оформить заказ"
        self.click_on_element_located(MainPageLocators.PLACE_ORDER_BUTTON, delay_time)
    @allure.step('click_on_crater_bun_button')
    def click_on_crater_bun_button(self, delay_time):  #Кликнуть по кратерной булке

        self.click_on_element_located(MainPageLocators.CRATER_BUN_ICON, delay_time)

    @allure.step('click_on_close_button_on_ingredient_detail')
    def click_on_close_button_on_ingredient_detail(self, delay_time):  #Кликнуть по крестику на окне с ингредиентами
        self.click_on_element_located(MainPageLocators.CLOSING_BUTTON_INGREDIENT_DETAILS, delay_time)

    @allure.step('click_on_close_button_on_ingredient_detail')
    def wait_of_vanishing_of_overlay(self, driver, delay_time):  #Ожидание пропадания всплывающего объекта
        WebDriverWait(driver, delay_time).until_not(EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))

    @allure.step('get_count_number_of_crater_bun_in_constructor')
    def get_count_number_of_crater_bun_in_constructor(self, delay_time):  # Получение значения счетчика Краторной булки
        count_number =int(self.find_element_located(MainPageLocators.COUNTER_OF_CRATER_BUN, delay_time).text)
        return count_number

    @allure.step('get_number_of_new_order_from_window')
    def get_number_of_new_order_from_window(self, delay_time):  # Получение значения счетчика Краторной булки
        for i in range(1, 200):
            number =int(self.find_element_located(MainPageLocators.ORDER_NUMBER_COUNTER_IN_WINDOW, 8).text)
            if number == 9999:
                pass
            else:
                break
        return number

    @allure.step('drag_and_drop_crater_bun')
    def drag_and_drop_crater_bun(self, delay_time):  # Перетащить краторную булку в корзину
        self.drag_and_drop_element(MainPageLocators.CRATER_BUN_ICON, MainPageLocators.ORDER_BUCKET_PLACE,
                                delay_time)

    @allure.step('click_on_enter_account_button')
    def find_enter_account_button(self, delay_time):  #Найти переход "Вход в Аккаунт"
        self.find_element_located(MainPageLocators.ENTER_ACCOUNT_BUTTON, delay_time)

    @allure.step('click_on_private_account_button')
    def click_on_private_account_button_main_page(self, delay_time):  #Кликнуть переход  на "Личный Кабинет"
        self.click_on_element_located(MainPageLocators.PRIVATE_ACCOUNT_BUTTON, delay_time)
    @allure.step('set_an_order_ui')
    def set_an_order_ui(self,driver, delay_time):
        WebDriverWait(driver, 20).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))

        self.drag_and_drop_element(MainPageLocators.CRATER_BUN_ICON, MainPageLocators.ORDER_BUCKET_PLACE, delay_time)
        WebDriverWait(driver, 200).until_not(EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))

        self.click_on_element_located(MainPageLocators.PLACE_ORDER_BUTTON, delay_time)


    @allure.step('close_card_with_new_order')
    def close_card_with_new_order(self, driver, delay_time):
        self.click_on_element_located(MainPageLocators.CLOSING_ORDER_CARD_BUTTON, delay_time)

    @allure.step('checking_of_presence_of_order_feed_main_headline')
    def checking_of_presence_of_ingredient_details_crater_bun(self, delay_time):
        result = self.find_element_presented(MainPageLocators.INGREDIENT_DETAILS_CRATER_BUN, delay_time)
        return result

    @allure.step('checking_of_presence_of_order_id_in_card')
    def checking_of_presence_of_order_id_header_in_the_card(self, delay_time):
        result = self.find_element_presented(MainPageLocators.ID_ORDER_HEADER, delay_time)
        return result

    @allure.step('checking_of_presence_of_order_id_in_card')
    def checking_of_existing_crater_bun_ingredient_details(self):
        result = self.check_exists_by_xpath(MainPageLocators.INGREDIENT_DETAILS_CRATER_BUN)
        return result


