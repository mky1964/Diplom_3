
from locators.constructor_locators import ConstructorLocators
from locators.order_feed_locators import OrderFeedLocators
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, new_user
from pages.main_page import MainPage
from pages.account_page import Account


class TestMainFunctions:

    @allure.title('test_passover_from_pr_acc_to_orders_feed')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Переход из Личного лабинета в Ленту Заказов')
    def test_passover_from_pr_account_to_orders_feed(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        main_page_1.click_on_private_account_button_main_page(60)
        account_1.click_on_orders_feed(60)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            OrderFeedLocators.ORDER_FEED_MAIN_HEADLINE)), f'Заголовок "Вход" не виден'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)

    @allure.title('test_passover_from_pr_account_to_constructor')
    @allure.description('Позитивный тест.Проверка основного функционала.'
                        ' Переход из Личного лабинета в Конструктор')
    def test_passover_from_pr_account_to_constructor(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        main_page_1.click_on_private_account_button_main_page(60)
        account_1.click_on_constructor_button_from_account(60)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            ConstructorLocators.ASSEMBLE_BURGER_HEADLINE)), f'Заголовок "Соберите бургер" не виден'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)

    @allure.title('test_in_constructor_get_ingredients_details_by_clicking_ingredient')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' В конструкторе если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_in_constructor_get_ingredients_details_by_clicking_ingredient(self, driver):
        main_page_1 = MainPage(driver)
        main_page_1.click_on_crater_bun_button(60)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            ConstructorLocators.INGREDIENT_DETAILS_CRATER_BUN)), f'Заголовок "Детали ингредиента" не виден'

    @allure.title('test_closing_ingredient_details')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' всплывающее окно  с ингредиентами закрывается кликом по крестику')
    def test_closing_ingredient_details(self, driver):
        main_page_1 = MainPage(driver)
        main_page_1.click_on_crater_bun_button(60)
        main_page_1.click_on_close_button_on_ingredient_detail(60)

        assert (main_page_1.check_exists_by_xpath(ConstructorLocators.INGREDIENT_DETAILS_CRATER_BUN) != True),\
            f'Окно с деталями ингредиента не закрывается'#Проверка отсутствия окна с ингредиентами после выхода из окна


    @allure.title('test_after_adding_of_ingredient_counter_add_1')
    @allure.description('Позитивный тест. Проверка основного функционала.'
                        ' при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_after_adding_of_ingredient_counter_add_1(self, driver):
        main_page_1 = MainPage(driver)
        initial_count_num = main_page_1.get_count_number_of_crater_bun_in_constructor(60)
        main_page_1.wait_of_vanishing_of_overlay(driver,60)
        main_page_1.drag_and_drop_crater_bun(60)
        final_count_num = main_page_1.get_count_number_of_crater_bun_in_constructor(60)
        delta = final_count_num - initial_count_num
        assert delta == 2, f'Счетчик ингредиента не работает'

    @allure.title('test_user_logins_and_places_an_order')
    @allure.description('Позитивный тест.Проверка основного функционала.'
                        ' залогиненный пользователь может оформить заказ')
    def test_user_logins_and_places_an_order(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        account_1.login_account_from_main_page(driver, new_user, 60)
        main_page_1.set_an_order_ui(driver, 60)
        order_number = main_page_1.get_number_of_new_order_from_window(60)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            ConstructorLocators.ID_ORDER_HEADER)) and (order_number != 9999), f'Идентификатор заказа" не виден на всплывающем окне'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)