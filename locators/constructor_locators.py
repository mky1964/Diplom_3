from selenium.webdriver.common.by import By

class ConstructorLocators:

    ASSEMBLE_BURGER_HEADLINE = (By.XPATH,
                                '//h1[@class="text text_type_main-large mb-5 mt-10" and text()="Соберите бургер"]')
    CRATER_BUN_ICON = (By.XPATH,
                       '//p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Краторная булка N-200i"]')
    INGREDIENT_DETAILS_CRATER_BUN = (By.XPATH,
                                 '//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    CLOSING_BUTTON_INGREDIENT_DETAILS = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button')
    COUNTER_OF_CRATER_BUN = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/div[1]/p')
    ORDER_BUCKET_PLACE = (By.XPATH, '//*[@id="root"]/div/main/section[2]')
    PLACE_ORDER_BUTTON = (By.XPATH,
                          '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    ID_ORDER_HEADER = (By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]')
    ORDER_NUMBER_COUNTER_IN_WINDOW = (By.XPATH,
                                      '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')