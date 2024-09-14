import time
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


class TestPasswordRestore:
    @allure.feature('test_restore_password_button')
    @allure.description('Позитивный тест. Восстановление пароля.'
                        ' Переход по кнопке "Восстановить пароль" на страницу восстановления пароля')
    def test_restore_password_button(self, driver):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        main_page_1.click_on_enter_account_button(5)
        account_1.click_on_restore_password_button(5)
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            AccountPageLocators.RESTORING_PASSWORD_HEADLINE)), f'Заголовок "Восстановление пароля" не виден'

    @allure.feature('test_set_email_when_restoring_password')
    @allure.description('Позитивный тест.Восстановление пароля. Ввод почты и клик по кнопке «Восстановить».'
                        ' Переход на новую страницу для замены пароля. Наличие кнопки "Сoхранить"')
    def test_set_email_when_restoring_password(self, driver, new_user):
        main_page_1 = MainPage(driver)
        time.sleep(3)
        account_1 = Account(driver)
        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        main_page_1.click_on_enter_account_button(5)
        account_1.click_on_restore_password_button(10)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            AccountPageLocators.RESTORING_PASSWORD_HEADLINE))
        account_1.set_text_to_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_EMAIL, new_user_with_accesstoken['email'],5)
        account_1.click_on_element_located(RestoringPasswordPageLocators.BUTTON_RESTORE, 5)
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PAGE_BUTTON_SAVE))

        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})




    @allure.feature('test_click_on_show_hide_button_password_placeholder')
    @allure.description('Позитивный тест. Восстановление пароля.'
                        ' Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_on_show_hide_button_password_placeholder(self, driver, new_user):
        main_page_1 = MainPage(driver)
        main_page_1.go_to_site(Constants.MAIN_PAGE_URL)
        time.sleep(3)
        account_1 = Account(driver)

        new_user_with_accesstoken = account_1.registration_of_new_user(new_user)
        main_page_1.click_on_enter_account_button(5)
        account_1.click_on_restore_password_button(5)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            AccountPageLocators.RESTORING_PASSWORD_HEADLINE))
        account_1.set_text_to_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_EMAIL, new_user_with_accesstoken['email'], 5)
        account_1.click_on_element_located(RestoringPasswordPageLocators.BUTTON_RESTORE, 5)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            RestoringPasswordPageLocators.BUTTON_RESTORE))
        main_page_1.click_on_element_located(RestoringPasswordPageLocators.RESTORING_PASSWORD_SHOW_HIDE_BUTTON_XPATH, 10)
        main_page_1.find_element_located(RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE, 10)
        assert WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE))

        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']})