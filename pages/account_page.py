import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage



class Account(BasePage):

    @allure.step('click_on_enter_account_button')
    def click_on_restore_password_button(self, delay_time):  #Кликнуть Восстановление пароля во вкладке "ВХОД" Личного кабинета
        self.click_on_element_located(AccountPageLocators.PASSWORD_RESTORE_BUTTON, delay_time)

    @allure.step('click_on_enter_account_button')
    def click_on_orders_history_button(self):  #Кликнуть История заказов из Личного кабинета
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.click_on_element_located(AccountPageLocators.ORDERS_HISTORY_BUTTON, 100)

    @allure.step('click_on_enter_account_button')
    def click_on_constructor_button_from_account(self, delay_time):  #Кликнуть конструктор
        self.click_on_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, delay_time)


    @allure.step('click_on_enter_account_button')
    def click_on_orders_feed(self):  #Кликнуть "Лента заказов"
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE,120)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.click_on_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
    @allure.step('login_account_from_main_page')
    def login_account_from_main_page(self, new_user, time_delay):#Залогинить пользователя из main_page
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE, 10)
        self.scroll_to_element_located(AccountPageLocators.CHEESE_WITH_MOLD, 100)
        self.scroll_to_element_located(AccountPageLocators.CRATER_BUN_ICON, 100)
        self.click_on_element_located(AccountPageLocators.PRIVATE_ACCOUNT_BUTTON, time_delay)
        self.find_element_located(AccountPageLocators.ENTER_BUTTON, 10)
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE, 10)
        self.set_text_to_element_located(AccountPageLocators.EMAIL_PLACEHOLDER, new_user['email'], time_delay)
        self.set_text_to_element_located(AccountPageLocators.PASSWORD_PLACEHOLDER, new_user['password'], time_delay)
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE, 10)
        self.find_element_located(AccountPageLocators.ENTER_BUTTON, 20)
        self.click_on_element_located(AccountPageLocators.ENTER_BUTTON, time_delay)





    @allure.step('login_account_from_main_page')
    def exit_from_account(self):#Залогинить пользователя из main_page
        self.wait_of_vanishing_of_overlay_base(AccountPageLocators.MODAL_OVERLAY_MAIN_PAGE,120)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.find_element_located(AccountPageLocators.ORDER_FEED_BUTTON, 100)
        self.find_element_located(AccountPageLocators.CONSTRUCTOR_BUTTON, 100)
        self.click_on_element_located(AccountPageLocators.EXIT_BUTTON_FROM_ACCOUNT, 100)

    @allure.step('checking_of_presence_of_order_history_button_in_private_account')
    def checking_of_presence_of_order_history_button_in_private_account(self, delay_time):
        result = self.find_element_presented(AccountPageLocators.ORDERS_HISTORY_BUTTON, delay_time)
        return result

    @allure.step('checking_of_presence_of_last_order_number_in_order_history')
    def checking_of_presence_of_the_latest_order_number_in_order_history(self, delay_time):
        result = self.find_element_presented(AccountPageLocators.LATEST_ORDER_NUMBER, delay_time)
        return result

    @allure.step('checking_of_presence_of_the_enter_button_in_constructor')
    def checking_of_presence_of_the_enter_button_in_login_window(self, delay_time):
        result = self.find_element_presented(AccountPageLocators.ENTER_BUTTON, delay_time)
        return result
