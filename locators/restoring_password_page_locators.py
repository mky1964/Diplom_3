from selenium.webdriver.common.by import By

class RestoringPasswordPageLocators:
    RESTORING_PASSWORD_PLACEHOLDER_EMAIL = (
        By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')#Плейсхолдер "EMAIL" на вкладке "Восстановление пароля - 1

    RESTORING_PASSWORD_PAGE_BUTTON_SAVE = (By.XPATH,
                                           '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Сохранить"]'
                                           )#Кнопка "Сохранить" на вкладке "Восстановление пароля - 2"
    BUTTON_RESTORE = (
        By.XPATH,
        '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Восстановить"]'
    )# Кнопка"Восстановить"  на вкладке "Восстановление пароля - 1"

    RESTORING_PASSWORD_SHOW_HIDE_BUTTON_XPATH = (By.XPATH,
                                                 '//div[@class="input__icon input__icon-action"]'
                                                 )# Кнопка "показать-скрыть" на плейсхолдере  Password на вкладке "Восстановление пароля - 2
    RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_NOT_ACTIVE = (By.XPATH,
                                                          '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]'
                                                          )#Не подсвеченный плейсхолдер Password
    RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE = (By.XPATH, '//div[contains(@class, "input pr-6 pl-6 input_type_text")]'
                                                      )#Подсвеченный плейсхолдер Password
    PASSWORD_RESTORE_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")#"Кнопка "Восстановить пароль" в Личном кабинете вкладка "Вход"
    RESTORING_PASSWORD_HEADLINE = (By.XPATH, "//h2[text()='Восстановление пароля']")#Хедлайн "Восстановление пароля" в Личном кабинете вкладка "Восстановление пароля"

