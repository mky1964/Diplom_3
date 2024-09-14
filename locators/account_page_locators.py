from selenium.webdriver.common.by import By

class AccountPageLocators:

    PASSWORD_RESTORE_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    RESTORING_PASSWORD_HEADLINE = (By.XPATH, "//h2[text()='Восстановление пароля']")

