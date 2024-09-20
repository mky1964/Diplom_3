import time
import allure
import requests
from selenium.webdriver.support.wait import WebDriverWait
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from locators.private_account_locators import PrivateAccountLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.main_page import MainPage
from conftest import new_user


class Account(BasePage):

    @allure.step('click_on_enter_account_button')
    def click_on_restore_password_button(self, delay_time):  #Кликнуть Восстановление пароля во вкладке "ВХОД" Личного кабинета
        self.click_on_element_located(AccountPageLocators.PASSWORD_RESTORE_BUTTON, delay_time)

    @allure.step('click_on_enter_account_button')
    def click_on_orders_history_button(self, delay_time):  #Кликнуть История заказов
        time.sleep(2)
        self.click_on_element_located(PrivateAccountLocators.ORDERS_HISTORY_BUTTON, delay_time)

    @allure.step('click_on_enter_account_button')
    def click_on_constructor_button_from_account(self, delay_time):  #Кликнуть История заказов
        time.sleep(2)
        self.click_on_element_located(PrivateAccountLocators.CONSTRUCTOR_BUTTON, delay_time)


    @allure.step('click_on_enter_account_button')
    def click_on_orders_feed(self, delay_time):  #Кликнуть "Лента заказов"
        time.sleep(3)
        self.click_on_element_located(PrivateAccountLocators.ORDER_FEED_BUTTON, delay_time)
    @allure.step('login_account_from_main_page')
    def login_account_from_main_page(self, driver, new_user, time_delay):#Залогинить пользователя из main_page
        main_page_1 = MainPage(driver)
        WebDriverWait(driver, 200).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))
        main_page_1.click_on_private_account_button_main_page(time_delay)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(PrivateAccountLocators.ENTER_BUTTON))
        WebDriverWait(driver, 200).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER, new_user['email'], time_delay)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER, new_user['password'], time_delay)
        WebDriverWait(driver, 200).until_not(
            EC.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY_MAIN_PAGE))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(PrivateAccountLocators.ENTER_BUTTON))
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, time_delay)


    @allure.step('login_account_from_main_page')
    def login_account_by_requests(self, new_user):#Залогинить пользователя из main_page
        result = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', json=new_user, timeout=120)
        print(result.json())
        print(result.status_code)

    @allure.step('login_account_from_main_page')
    def exit_from_account(self, driver, delay_time):#Залогинить пользователя из main_page
        account_1 = Account(driver)
        account_1.click_on_element_located(PrivateAccountLocators.EXIT_BUTTON_FROM_ACCOUNT, delay_time)
