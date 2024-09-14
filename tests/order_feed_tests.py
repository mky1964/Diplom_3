import time
import requests
from locators.main_page_locators  import MainPageLocators
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
from locators.history_of_orders_locators import HistoryOfOrderLocators
class TestOrderFeed:
    @allure.feature('test_opening_order_details_in_order_feed')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_opening_order_details_in_order_feed(self, driver, new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        """new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        print(new_user_with_accesstoken)
        main_page_1.click_on_private_account_button(5)
        time.sleep(3)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER, new_user_with_accesstoken['email'],5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER, new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)"""
        main_page_1.click_on_private_account_button(10)
        time.sleep(3)
        account_1.click_on_element_located(PrivateAccountLocators.ORDER_FEED_BUTTON, 5)
        account_1.click_on_element_located(OrderFeedLocators.ORDER_IN_ORDER_FEED_NUM_1, 5)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            OrderFeedLocators.ORDER_DETAIL_CARD_NUMBER)), f'Карточка с ингредиентами не появилась'


    @allure.feature('test_order_num_from_order_history_present_in_order_feed')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_num_from_order_history_present_in_order_feed(self, driver, new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        order_ingredients = {'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients, headers={'Authorization': new_user_with_accesstoken['token']})
        print(new_user_with_accesstoken)
        main_page_1.click_on_private_account_button(5)
        time.sleep(3)

        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER, new_user_with_accesstoken['email'],5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER, new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)
        main_page_1.click_on_private_account_button(10)
        time.sleep(5)
        account_1.click_on_element_located(PrivateAccountLocators.ORDERS_HISTORY_BUTTON, 5)
        time.sleep(5)
        number_order_in_history = account_1.find_element_presented(HistoryOfOrderLocators.FIRST_ORDER_NUMBER, 10).text
        #print(number_order_in_history)
        account_1.click_on_element_located(PrivateAccountLocators.ORDER_FEED_BUTTON, 10)
        num = account_1.find_element_presented((By.XPATH, f'//*[@id="root"]/div/main/div/div/ul/li[{'1'}]'), 2).text
        #print(num)
        for i in range(1, 50):
            num = account_1.find_element_presented((By.XPATH, f'//*[@id="root"]/div/main/div/div/ul/li[{i}]'), 2).text
            if number_order_in_history in num:
                result = True
                #print(result)
                break
            else:
                result = False
        assert result == True, f'Номер из "Истории заказов" отсутствует в "Ленте заказов"'

        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})



    @allure.feature('test_all_time_counter_adds_1_after_new_order')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_all_time_counter_adds_1_after_new_order(self, driver, new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        order_ingredients = {
            'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                      headers={'Authorization': new_user_with_accesstoken['token']})
        print(new_user_with_accesstoken)
        main_page_1.click_on_private_account_button(5)
        time.sleep(3)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER,
                                                new_user_with_accesstoken['email'], 5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER,
                                                new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)
        main_page_1.click_on_private_account_button(10)
        WebDriverWait(driver, 60).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))
        account_1.click_on_element_located(PrivateAccountLocators.ORDER_FEED_BUTTON, 20)
        number_of_orders_all_time_1 = int(account_1.find_element_presented(OrderFeedLocators.ORDER_NUMBER_ALL_TIME, 5).text)
        print(number_of_orders_all_time_1)
        requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                      headers={'Authorization': new_user_with_accesstoken['token']})
        number_of_orders_all_time_2 = int(account_1.find_element_presented(OrderFeedLocators.ORDER_NUMBER_ALL_TIME, 5).text)
        print(number_of_orders_all_time_2)
        delta = number_of_orders_all_time_2 - number_of_orders_all_time_1#Изменение числа заказов за всё время
        assert delta > 0, f'Число заказов за всё время не изменилось после добавления заказа'

        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})

    @allure.feature('test_today_counter_adds_1_after_new_order')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_counter_adds_1_after_new_order(self, driver, new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        order_ingredients = {
            'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                      headers={'Authorization': new_user_with_accesstoken['token']})
        print(new_user_with_accesstoken)
        main_page_1.click_on_private_account_button(5)
        time.sleep(3)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER,
                                                new_user_with_accesstoken['email'], 5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER,
                                                new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        time.sleep(5)
        main_page_1.click_on_private_account_button(10)
        WebDriverWait(driver, 60).until_not(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))
        account_1.click_on_element_located(PrivateAccountLocators.ORDER_FEED_BUTTON, 20)
        number_of_orders_today_1 = int(
            account_1.find_element_presented(OrderFeedLocators.ORDER_NUMBER_TODAY, 5).text)
        print(number_of_orders_today_1)
        requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                        headers={'Authorization': new_user_with_accesstoken['token']})
        number_of_orders_today_2 = int(
            account_1.find_element_presented(OrderFeedLocators.ORDER_NUMBER_TODAY, 5).text)
        print(number_of_orders_today_2)
        delta = number_of_orders_today_2 - number_of_orders_today_1  # Изменение числа заказов за всё время
        assert delta == 1, f'Число заказов за всё время не изменилось после добавления заказа'

        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})


    @allure.feature('test_after_placing_an_order_number_appears_in_work')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' после оформления заказа его номер появляется в разделе В работе')
    def test_after_placing_an_order_number_appears_in_work(self, driver, new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        order_ingredients = {
            'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}

        main_page_1.click_on_private_account_button(5)
        time.sleep(3)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.EMAIL_PLACEHOLDER,
                                                new_user_with_accesstoken['email'], 5)
        main_page_1.set_text_to_element_located(PrivateAccountLocators.PASSWORD_PLACEHOLDER,
                                                new_user_with_accesstoken['password'], 5)
        main_page_1.click_on_element_located(PrivateAccountLocators.ENTER_BUTTON, 5)
        WebDriverWait(driver, 10).until_not(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')))
        account_1.click_on_element_located(MainPageLocators.ORDERS_FEED_FROM_MAIN_BUTTON, 30)
        time.sleep(1)
        token = new_user_with_accesstoken['token']
        response = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                        headers={'Authorization': token})
        time.sleep(10)
        number = account_1.find_element_presented(OrderFeedLocators.ORDER_NUMBER_IN_WORK,30).text
        order_number_in_work_actual = number
        number = list(response.json().values())[-1]['number']
        order_number_in_work_expected = f'0{number}'
        assert order_number_in_work_expected == order_number_in_work_actual
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})
