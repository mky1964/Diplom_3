from selenium.webdriver.common.by import By

class MainPageLocators:

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PRIVATE_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account" ]')
    ORDERS_FEED_FROM_MAIN_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')

