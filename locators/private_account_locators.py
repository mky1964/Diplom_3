from selenium.webdriver.common.by import By

class PrivateAccountLocators:

    ORDERS_HISTORY_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a')
    #"История Заказов" - кнопка в личном кабинете
    ORDER_FEED_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/feed"]')
    EMAIL_PLACEHOLDER = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="name"]')
    PASSWORD_PLACEHOLDER = (By.XPATH,
                            '//input[@class="text input__textfield text_type_main-default" and @name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" ]')
    ORDER_WINDOW = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]')
    EXIT_BUTTON_FROM_ACCOUNT = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]')


