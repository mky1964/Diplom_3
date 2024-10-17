import allure
from pages.main_page import MainPage
from pages.account_page import Account
from conftest import driver,  new_user_registration_without_order
from helpers import set_order_helper


class TestPrivateAccount:

    @allure.title('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь переходит по клику на «Личный кабинет» на страницу авторизации Личного лабинета.'
                        ' Авторизируется. Опять переходит в личный кабинет. Обнаруживается кгнопка "История заказов". Пользователь авторизирован')
    def test_passover_via_pr_acc_button_to_pr_acc(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        set_order_helper(new_user_with_accesstoken,100)
        account_1.login_account_from_main_page(new_user_with_accesstoken, 60)
        main_page_1.click_on_private_account_button_main_page()
        assert account_1.checking_of_presence_of_order_history_button_in_private_account(30), f'Не перешли в Личный кабинет'

    @allure.title('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный и авторизированный пользователь переходит по кнопке "История Заказов"')
    def test_passover_via_pr_acc_to_orders_history(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        set_order_helper(new_user_with_accesstoken, 100)
        account_1.login_account_from_main_page(new_user_with_accesstoken, 60)
        main_page_1.click_on_private_account_button_main_page()
        account_1.click_on_orders_history_button()
        assert account_1.checking_of_presence_of_the_latest_order_number_in_order_history(60), f'Не перешли в историю заказов'

    @allure.title('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь выходит из Личного Кабинета по кнопке "Выход"')
    def test_exit_from_account(self, driver, new_user_registration_without_order):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = new_user_registration_without_order
        set_order_helper(new_user_with_accesstoken, 100)
        account_1.login_account_from_main_page(new_user_with_accesstoken, 60)
        main_page_1.click_on_private_account_button_main_page()
        account_1.exit_from_account()
        assert account_1.checking_of_presence_of_the_enter_button_in_login_window(30), f' не произошел переход в Constructor'




