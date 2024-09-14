import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage



class Account(BasePage):

    @allure.step('click_on_enter_account_button')
    def click_on_restore_password_button(self, delay_time=5):  #Кликнуть стрелку с вопросом
        self.click_on_element_located(AccountPageLocators.PASSWORD_RESTORE_BUTTON, delay_time=5)
