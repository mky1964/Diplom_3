
import allure
from conftest import driver, new_user_registration_without_order
from pages.main_page import MainPage
from pages.account_page import Account
from pages.order_feed_page import OrderFeedPage


class TestMainFunctions:

    @allure.title('test_passover_from_pr_acc_to_orders_feed')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Переход из Личного лабинета в Ленту Заказов')
    def test_passover_from_pr_account_to_orders_feed(self, driver):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        order_1 = OrderFeedPage(driver)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_orders_feed()
        assert order_1.checking_of_presence_of_order_feed_main_headline(30), f'Заголовок "Вход" не виден'


    @allure.title('test_passover_from_pr_account_to_constructor')
    @allure.description('Позитивный тест.Проверка основного функционала.'
                        ' Переход из Личного лабинета в Конструктор')
    def test_passover_from_pr_account_to_constructor(self, driver):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        order_1 = OrderFeedPage(driver)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_constructor_button_from_account(60)
        assert order_1.checking_of_presence_assemble_burger_in_constructor(30), f'Заголовок "Соберите бургер" не виден'


    @allure.title('test_in_constructor_get_ingredients_details_by_clicking_ingredient')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' В конструкторе если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_in_constructor_get_ingredients_details_by_clicking_ingredient(self, driver):
        main_page_1 = MainPage(driver)
        main_page_1.find_enter_account_button(60)
        main_page_1.click_on_crater_bun_button()
        assert main_page_1.checking_of_presence_of_ingredient_details_crater_bun(30), f'Заголовок "Детали ингредиента" не виден'

    @allure.title('test_closing_ingredient_details')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' всплывающее окно  с ингредиентами закрывается кликом по крестику')
    def test_closing_ingredient_details(self, driver):
        main_page_1 = MainPage(driver)
        main_page_1.find_enter_account_button(60)
        main_page_1.click_on_crater_bun_button()
        main_page_1.click_on_close_button_on_ingredient_detail(300)
        assert (main_page_1.checking_of_existing_crater_bun_ingredient_details != True),\
            f'Окно с деталями ингредиента не закрывается'#Проверка отсутствия окна с ингредиентами после выхода из окна


    @allure.title('test_after_adding_of_ingredient_counter_add_1')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_after_adding_of_ingredient_counter_add_1(self, driver):
        main_page_1 = MainPage(driver)
        main_page_1.find_enter_account_button(60)
        initial_count_num = main_page_1.get_count_number_of_crater_bun_in_constructor(60)
        main_page_1.wait_of_vanishing_of_overlay(60)
        main_page_1.drag_and_drop_crater_bun(100)
        main_page_1.find_enter_account_button(60)
        final_count_num = main_page_1.get_count_number_of_crater_bun_in_constructor(120)
        delta = final_count_num - initial_count_num
        assert delta == 2, f'Счетчик ингредиента не работает'

    @allure.title('test_user_logins_and_places_an_order')
    @allure.description('Позитивный тест.Проверка основного функционала.'
                        ' залогиненный пользователь может оформить заказ')
    def test_user_logins_and_places_an_order(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        main_page_1.find_enter_account_button(60)
        account_1.login_account_from_main_page(new_user_with_accesstoken, 120)
        main_page_1.set_an_order_ui()
        order_number = main_page_1.get_number_of_new_order_from_window(60)
        assert main_page_1.checking_of_presence_of_order_id_header_in_the_card(120) and (order_number != 9999), f'Идентификатор заказа" не виден на всплывающем окне'


