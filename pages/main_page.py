import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('click_on_enter_account_button')
    def click_on_enter_account_button(self, delay_time=5):  #Кликнуть переход "Вход в Аккаунт"
        self.click_on_element_located(MainPageLocators.ENTER_ACCOUNT_BUTTON, delay_time=5)

    @allure.step('click_on_private_account_button')
    def click_on_private_account_button(self, delay_time=5):  #Кликнуть переход  на "Личный Кабинет"
        self.click_on_element_located(MainPageLocators.PRIVATE_ACCOUNT_BUTTON, delay_time=5)