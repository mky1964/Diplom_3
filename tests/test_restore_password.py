import requests
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, new_user
from pages.main_page import MainPage
from pages.account_page import Account
from locators.constants import Constants
from locators.account_page_locators import AccountPageLocators
from locators.restoring_password_page_locators import RestoringPasswordPageLocators
from pages.restoring_password_page import RestorePassword
class TestPasswordRestore:

    @allure.title('test_restore_password_button')
    @allure.description('Позитивный тест. Восстановление пароля.'
                        ' Переход по кнопке "Восстановить пароль" на страницу восстановления пароля')
    def test_restore_password_button(self, driver):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        main_page_1.find_enter_account_button(20)
        main_page_1.click_on_private_account_button_main_page(30)#Кликнуть переход "Вход в Аккаунт" из Main page
        account_1.click_on_restore_password_button(30)#Кликнуть Восстановление пароля во вкладке "ВХОД" Личного кабинета
        assert WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            AccountPageLocators.RESTORING_PASSWORD_HEADLINE)), f'Заголовок "Восстановление пароля" не виден'


    @allure.title('test_set_email_when_restoring_password')
    @allure.description('Позитивный тест.Восстановление пароля. Ввод почты и клик по кнопке «Восстановить».'
                        ' Переход на новую страницу для замены пароля. Наличие кнопки "Сoхранить"')
    def test_set_email_when_restoring_password(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        restore_1 = RestorePassword(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        main_page_1.find_enter_account_button(20)
        main_page_1.click_on_enter_account_button(30)#Кликнуть переход "Вход в Аккаунт" из Main page
        account_1.click_on_restore_password_button(30)#Кликнуть Восстановление пароля во вкладке "ВХОД" Личного кабинета
        restore_1.set_email_at_restoring_password_page(driver, new_user_with_accesstoken, 60)
        restore_1.click_on_restore_button_on_restore_password_page_1(60)
        assert WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PAGE_BUTTON_SAVE)), 'Не произошел переход на страницу восстановления пароля_2'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)

    @allure.title('test_click_on_show_hide_button_password_placeholder')
    @allure.description('Позитивный тест. Восстановление пароля.'
                        ' Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_on_show_hide_button_password_placeholder(self, driver, new_user):
        main_page_1 = MainPage(driver)
        account_1 = Account(driver)
        restore_1 = RestorePassword(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        main_page_1.find_enter_account_button(20)
        main_page_1.click_on_enter_account_button(30)#Кликнуть переход "Вход в Аккаунт" из Main page
        account_1.click_on_restore_password_button(30)#Кликнуть Восстановление пароля во вкладке "ВХОД" Личного кабинета
        restore_1.set_email_at_restoring_password_page(driver, new_user_with_accesstoken, 60)#Ввод EMAIL на странице восстановления пароля -1
        restore_1.click_on_restore_button_on_restore_password_page_1(60)# Клик по кнопке "Восстановить"  на вкладке "Восстановление пароля - 1"
        restore_1.click_on_show_hide_button_on_placeholder_password_restore_page_2(60) # Клик по кнопке "показать-скрыть" на плейсхолдере  Password на вкладке "Восстановление пароля - 2
        restore_1.find_highlighted_password_placeholder(60)
        assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE)), 'Плейсхолдер не подсвечивается при клике на него'
        main_page_1.deleting_of_new_user(new_user_with_accesstoken)