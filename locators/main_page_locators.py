from selenium.webdriver.common.by import By

class MainPageLocators:

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")#Кнопка  "Войти в аккаунт" из Main page
    PRIVATE_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account" ]')#Кнопка "Личный кабинет" из Main page
    ORDERS_FEED_FROM_MAIN_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')#"Лента заказов" из Main page
    MODAL_OVERLAY_MAIN_PAGE = (By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')
    PLACE_ORDER_BUTTON = (By.XPATH,
                          '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    CRATER_BUN_ICON = (By.XPATH,
                       '//p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Краторная булка N-200i"]')
    CLOSING_BUTTON_INGREDIENT_DETAILS = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button')
    COUNTER_OF_CRATER_BUN = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]/div/p[@class="counter_counter__num__3nue1"]')
    ORDER_NUMBER_COUNTER_IN_WINDOW = (By.XPATH,
                                      '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    CLOSING_ORDER_CARD_BUTTON = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_BUCKET_PLACE = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]')
    INGREDIENT_DETAILS_CRATER_BUN = (By.XPATH,
                                 '//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    ID_ORDER_HEADER = (By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]')



