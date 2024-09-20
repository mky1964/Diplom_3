from selenium.webdriver.common.by import By

class OrderFeedLocators:



    ORDER_FEED_MAIN_HEADLINE = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]')#"ЛЕНТА ЗАКАЗОВ" - на странице Ленты заказов
    ORDER_IN_ORDER_FEED_NUM_1 = (By.XPATH, '//li[1][@class="OrderHistory_listItem__2x95r mb-6"]')#Заказ (первый сверху) в ленте
    ORDER_DETAIL_CARD_NUMBER = (By.XPATH, '//p[@class="text text_type_digits-default mb-10 mt-5"]')#Номер в карточке ингредиентов в Ленте заказов
    ORDER_NUMBER_ALL_TIME = (By.XPATH,
                                  '//div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    #Количество заказов за всё время
    ORDER_NUMBER_TODAY = (By.XPATH, '//div[3]/p[2][@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')#Количество заказов на сегодня
    ORDER_READY_NUMBER = (By.XPATH, '//li[1][@class="text text_type_digits-default mb-2"]')

    ORDER_NUMBER_IN_WORK = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li')

