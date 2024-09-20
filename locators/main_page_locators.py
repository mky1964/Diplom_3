from selenium.webdriver.common.by import By

class MainPageLocators:

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")#Кнопка  "Войти в аккаунт" из Main page
    PRIVATE_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account" ]')#Кнопка "Личный кабинет" из Main page
    ORDERS_FEED_FROM_MAIN_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')#"Лента заказов" из Main page
    MODAL_OVERLAY_MAIN_PAGE = (By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')


