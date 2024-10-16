from selenium.webdriver.common.by import By

class AccountPageLocators:

    PASSWORD_RESTORE_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")#"Кнопка "Восстановить пароль" в Личном кабинете вкладка "Вход"
    RESTORING_PASSWORD_HEADLINE = (By.XPATH, "//h2[text()='Восстановление пароля']")#Хедлайн "Восстановление пароля" в Личном кабинете вкладка "Восстановление пароля"
    ORDERS_HISTORY_BUTTON = (By.XPATH, '//div/nav/ul/li[2]/a')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/feed"]')
    MODAL_OVERLAY_MAIN_PAGE = (By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]')
    PRIVATE_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account" ]')#Кнопка "Личный кабинет" из Main page
    EMAIL_PLACEHOLDER = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="name"]')
    PASSWORD_PLACEHOLDER = (By.XPATH,
                            '//input[@class="text input__textfield text_type_main-default" and @name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" ]')
    EXIT_BUTTON_FROM_ACCOUNT = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    LATEST_ORDER_NUMBER = (By.XPATH,
                           '//li[1]/a/div[@class="OrderHistory_textBox__3lgbs mb-6"]/p[@class="text text_type_digits-default"]')  # Номер последнего заказа в истории заказов

    CHEESE_WITH_MOLD = (By.XPATH, "//img[@alt='Сыр с астероидной плесенью']")
    CRATER_BUN_ICON = (By.XPATH,
                       '//p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Краторная булка N-200i"]')