import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.private_account_locators import PrivateAccountLocators
from pages.main_page import MainPage
from pages.account_page import Account
from conftest import driver, new_user
from locators.history_of_orders_locators import HistoryOfOrderLocators



class TestPrivateAccount:

    @allure.title('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь переходит по клику на «Личный кабинет» на страницу авторизации Личного лабинета.'
                        ' Авторизируется. Опять переходит в личный кабинет. Обнаруживается кгнопка "История заказов". Пользователь авторизирован')
    def test_passover_via_pr_acc_button_to_pr_acc(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        account_1.login_account_from_main_page(driver, new_user, 60)
        main_page_1.set_an_order_api(new_user_with_accesstoken,  60)
        main_page_1.click_on_private_account_button_main_page(60)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            PrivateAccountLocators.ORDERS_HISTORY_BUTTON)), f'Не перешли в Личный кабинет'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)

    @allure.title('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный и авторизированный пользователь переходит по кнопке "История Заказов"')
    def test_passover_via_pr_acc_to_orders_history(self, driver, new_user):

        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        account_1.login_account_from_main_page(driver, new_user, 60)
        main_page_1.set_an_order_api(new_user_with_accesstoken,  100)
        main_page_1.click_on_private_account_button_main_page(60)
        account_1.click_on_orders_history_button(100)
        assert WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            HistoryOfOrderLocators.LATEST_ORDER_NUMBER)), f'Не перешли в историю заказов'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)


    @allure.title('test_passover_via_pr_acc_button_to_pr_acc')
    @allure.description('Позитивный тест.Личный кабинет.'
                        ' Зарегистрированный пользователь выходит из Личного Кабинета по кнопке "Выход"')
    def test_exit_from_account(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        account_1.login_account_from_main_page(driver, new_user, 60)
        main_page_1.set_an_order_api(new_user_with_accesstoken,  60)
        main_page_1.click_on_private_account_button_main_page(100)
        account_1.exit_from_account(driver, 100)
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            PrivateAccountLocators.ENTER_BUTTON)), f' не произошел переход в Constructor'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)



