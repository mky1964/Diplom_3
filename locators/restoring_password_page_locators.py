from selenium.webdriver.common.by import By

class RestoringPasswordPageLocators:
    RESTORING_PASSWORD_PLACEHOLDER_EMAIL = (
        By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input')

    RESTORING_PASSWORD_PAGE_BUTTON_SAVE = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    BUTTON_RESTORE = (
        By.XPATH, '*//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    #RESTORING_PASSWORD_PLACEHOLDER_PASSWORD = (By.XPATH, '*//input[@name="Введите новый пароль"]')
    RESTORING_PASSWORD_SHOW_HIDE_BUTTON_XPATH = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/div')
    RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_NOT_ACTIVE = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]')
    RESTORING_PASSWORD_PLACEHOLDER_PASSWORD_ACTIVE = (By.XPATH, '//div[contains(@class, "input pr-6 pl-6 input_type_text")]' )
