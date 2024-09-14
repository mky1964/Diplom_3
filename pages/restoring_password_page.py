import allure
from locators.account_page_locators import AccountPageLocators
from locators.constants import Constants
from locators.restoring_password_page_locators import RestoringPasswordPageLocators
from pages.account_page import Account
from pages.base_page import BasePage
from pages.main_page import MainPage


class RestorePassword(BasePage):



    @allure.step('click_on_restore_button_at_restore_password_page')
    def click_on_restore_button_at_restore_password_page(self, delay_time=5):  #Кликнуть кнопку "Восстановить" на вкладке "Восстановление пароля"
        self.click_on_element_located(AccountPageLocators.PASSWORD_RESTORE_BUTTON, delay_time=5)