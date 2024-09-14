from selenium.webdriver.common.by import By

class OrderFeedLocators:

    ORDER_IN_ORDER_FEED_NUM = []

    ORDER_FEED_MAIN_HEADLINE = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]')#"ЛЕНТА ЗАКАЗОВ" - на странице Ленты заказов
    ORDER_IN_ORDER_FEED_NUM_1 = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]')#Заказ в ленте
    #ORDER_DETAIL_ORDER_NUMBER = (By.XPATH, '//p[@class="text text_type_digits-default mb-10 mt-5"]/text()[2]')#Номер заказа на карточке без "#0"
    #ORDER_NUMBER_TAG_1 = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a/div[1]/p[1]')#Номер последнего заказа в Ленте заказаов
    ORDER_DETAIL_CARD_NUMBER = (By.XPATH, '//p[@class="text text_type_digits-default mb-10 mt-5"]')#Номер в карточке ингредиентов в Ленте заказов
    ORDER_NUMBER_ALL_TIME = (By.XPATH,
                                  '//div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    #Количество заказов за всё время
    ORDER_NUMBER_TODAY = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/p[2]')#Количество заказов на сегодня
    ORDER_READY_NUMBER = (By.XPATH, '//li[1][@class="text text_type_digits-default mb-2"]')# //*[@id="root"]/div/main/div/div/div/div[1]/ul[1]/li[1]

    ORDER_NUMBER_IN_WORK = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li')

