import allure
from locators.restoring_password_page_locators import RestoringPasswordPageLocators
from pages.base_page import BasePage



class RestorePassword(BasePage):

    @allure.step('click_on_restore_button_at_restore_password_page')
    def click_on_restore_button_at_restore_password_page(self, delay_time):  #Кликнуть кнопку "Восстановить" на вкладке "Восстановление пароля"
        self.click_on_element_located(RestoringPasswordPageLocators.PASSWORD_RESTORE_BUTTON, delay_time)

    @allure.step('set_email_at_restoring_password_page')
    def set_email_at_restoring_password_page(self, new_user_with_accesstoken,  delay_time):  #Ввод EMAIL на вкладке "Восстановление пароля"
        self.find_element_presented(RestoringPasswordPageLocators.RESTORING_PASSWORD_HEADLINE, delay_time)
        self.set_text_to_element_located(
            RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_EMAIL, new_user_with_accesstoken['email'], delay_time)
    @allure.step('click_on_restore_button_on_restore_password_page_1')
    def click_on_restore_button_on_restore_password_page_1(self, delay_time): # Клик по Кнопке "Восстановить"  на вкладке "Восстановление пароля - 1"
        self.click_on_element_located(RestoringPasswordPageLocators.BUTTON_RESTORE, delay_time)

    @allure.step('click_on_restore_button_on_restore_password_page_1')
    def click_on_show_hide_button_on_placeholder_password_restore_page_2(self, delay_time): # Клик по кнопке "показать-скрыть" на плейсхолдере  Password на вкладке "Восстановление пароля - 2
        self.click_on_element_located(RestoringPasswordPageLocators.RESTORING_PASSWORD_SHOW_HIDE_BUTTON_XPATH, delay_time)

    @allure.step('find_highlighted_password_placeholder')
    def find_highlighted_password_placeholder(self, delay_time):#Дождатся подсвеченного плейсхолдера Password
        self.find_element_located(RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE, delay_time)

    @allure.step('checking_of_presence_of_passover_restoring_headline')
    def checking_of_presence_of_password_restoring_headline(self, delay_time):
        result = self.find_element_presented(RestoringPasswordPageLocators.RESTORING_PASSWORD_HEADLINE, delay_time)
        return result

    @allure.step('checking_of_presence_of_save_button_on_restoring_password_page')
    def checking_of_presence_of_save_button_on_restoring_password_page(self, delay_time):
        result = self.find_element_presented(RestoringPasswordPageLocators.RESTORING_PASSWORD_PAGE_BUTTON_SAVE, delay_time)
        return result

    @allure.step('checking_of_presence_of_active_password_placeholder_on_restoring_password_page')
    def checking_of_presence_of_active_password_placeholder_on_restoring_password_page(self, delay_time):
        result = self.find_element_presented(RestoringPasswordPageLocators.RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE, delay_time)
        return result


