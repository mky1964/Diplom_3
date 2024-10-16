from selenium.webdriver.common.by import By


class HistoryOfOrderLocators:

    LATEST_ORDER_NUMBER = (By.XPATH, '//li[1]/a/div[@class="OrderHistory_textBox__3lgbs mb-6"]/p[@class="text text_type_digits-default"]')#Номер последнего заказа в истории заказов
