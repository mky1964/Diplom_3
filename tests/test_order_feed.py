import allure
from conftest import driver,  new_user_registration_without_order
from pages.account_page import Account
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.history_of_orders_page import HistoryOfOrdersPage
from helpers import  set_order_helper


class TestOrderFeed:


    @allure.title('test_opening_order_details_in_order_feed')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_opening_order_details_in_order_feed(self, driver):
        main_page_1 = MainPage(driver)
        order_1 = OrderFeedPage(driver)
        main_page_1.click_on_order_feed_from_main_page()
        order_1.click_on_the_first_order_card_in_order_feed(60)
        assert order_1.checking_of_presence_of_order_details_card_number(60), f'Карточка с ингредиентами не появилась'


    @allure.title('test_order_num_from_order_history_present_in_order_feed')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_num_from_order_history_present_in_order_feed(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        history_1 = HistoryOfOrdersPage(driver)
        order_feed_1 = OrderFeedPage(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        account_1.login_account_from_main_page(new_user_with_accesstoken, 60)
        set_order_helper(new_user_with_accesstoken, 100)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_orders_history_button()
        latest_order_number_in_history = history_1.get_order_latest_order_number_in_history_of_orders(60)
        account_1.click_on_orders_feed()
        number_in_order_feed = order_feed_1.find_number_in_order_feed_by_order_number_from_history(latest_order_number_in_history)
        assert (latest_order_number_in_history in number_in_order_feed), 'Номер из истории заказов не найдегн в Ленте заказов'

    @allure.title('test_all_time_counter_adds_1_after_new_order')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_all_time_counter_adds_1_after_new_order(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        order_feed_1 = OrderFeedPage(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        account_1.login_account_from_main_page(new_user_with_accesstoken, 60)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_orders_feed()
        number_of_orders_all_time_1 = order_feed_1.get_number_of_orders_all_time_in_order_feed()
        set_order_helper(new_user_with_accesstoken, 100)
        number_of_orders_all_time_2 = order_feed_1.get_number_of_orders_all_time_in_order_feed()
        delta = number_of_orders_all_time_2 - number_of_orders_all_time_1#Изменение числа заказов за всё время
        assert delta > 0, f'Число заказов за всё время не изменилось после добавления заказа'

    @allure.title('test_today_counter_adds_1_after_new_order')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_counter_adds_1_after_new_order(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        order_feed_1 = OrderFeedPage(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        account_1.login_account_from_main_page(new_user_registration_without_order, 60)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_orders_feed()
        number_of_orders_today_1 = order_feed_1.get_number_of_orders_today_in_order_feed()
        set_order_helper(new_user_with_accesstoken, 100)
        number_of_orders_today_2 = order_feed_1.get_number_of_orders_today_in_order_feed()
        delta = number_of_orders_today_2 - number_of_orders_today_1  # Изменение числа заказов за всё время
        assert delta == 1, f'Число заказов за сегодня не изменилось после добавления заказа'

    @allure.title('test_after_placing_an_order_number_appears_in_work')
    @allure.description('Позитивный тест.Лента заказов.'
                        ' после оформления заказа его номер появляется в разделе В работе')
    def test_after_placing_an_order_number_appears_in_work(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        order_feed_1 = OrderFeedPage(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        account_1.login_account_from_main_page(new_user_with_accesstoken, 120)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_orders_feed()
        response_set_order = set_order_helper(new_user_with_accesstoken, 120)
        order_number_in_work_expected = order_feed_1.get_orders_number_in_work_in_order_feed_expected(response_set_order)
        order_number_in_work_actual = order_feed_1.get_orders_number_in_work_in_order_feed_actual()
        assert order_number_in_work_actual == order_number_in_work_expected, 'Номер заказа не обнаружен в разделе "В работе'





