from selenium.webdriver.common.by import By

class AccountPageLocators:

    PASSWORD_RESTORE_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")#"Кнопка "Восстановить пароль" в Личном кабинете вкладка "Вход"
    RESTORING_PASSWORD_HEADLINE = (By.XPATH, "//h2[text()='Восстановление пароля']")#Хедлайн "Восстановление пароля" в Личном кабинете вкладка "Восстановление пароля"

