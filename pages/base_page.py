
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators.constants import Constants
import requests

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    @allure.step('go_to_site')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step('find_element_located')
    def find_element_located(self, locator, delay_time):
        return WebDriverWait(self.driver, delay_time).until(EC.visibility_of_element_located(locator),
                                                            message=f'Not found {locator}')

    @allure.step('find_element_located')
    def find_element_presented(self, locator, delay_time):
        return WebDriverWait(self.driver, delay_time).until(EC.presence_of_element_located(locator),
                                                            message=f'Not found {locator}')

    @allure.step('scroll_to_element_located')
    def scroll_to_element_located(self, driver, locator, delay_time):
        element = self.find_element_located(locator, delay_time)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, delay_time).until(EC.visibility_of_element_located(locator),
                                                            message=f'Not found {locator}')

    @allure.step('click_on_element_located')
    def click_on_element_located(self, locator, delay_time):
        element = self.find_element_located(locator, delay_time)
        element.click()

    @allure.step('get_text_from_element_located')
    def get_text_from_element_located(self, locator):
        return self.find_element_located(locator, delay_time=5).text

    @allure.step('set_text_to_element_located')
    def set_text_to_element_located(self, locator, text, delay_time):
        element = self.find_element_located(locator, delay_time)
        return element.send_keys(text)

    @allure.step('drag_and_drop_element')
    def drag_and_drop_element(self, element_from, element_to, delay_time):
        from_element = self.find_element_located(element_from, delay_time=10)
        to_element = self.find_element_located(element_to, delay_time)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()



    @allure.step('registration_of_new_user')
    def registration_of_new_user(self, new_user):
        #Регистрация нового пользователя. Возвращает dict с email, password, name, accsessToken

        new_user_1 = new_user
        for i in range(1, 100):
            response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user_1, timeout=120)
            if response.status_code != 200:
                pass
            else:
                response_1 = response.json()
                response_2 = response_1.values()
                accessToken = list(response_2)[2]
                new_user_1['token'] = accessToken
                break
        return new_user_1



    @allure.step('check_exists_by_xpath')
    def check_exists_by_xpath(self, locator):
        try:
            self.find_element_located(locator, 5)
            result = True
        except Exception:
            result = False
        return result

    @allure.step('deleting_of_new_user')
    def deleting_of_new_user(self, new_user_with_accesstoken):
        requests.delete(Constants.DELETE_USER_URL, headers={'Authorization': new_user_with_accesstoken['token']},timeout=10)


    @allure.step('registration_of_new_user')
    def creating_an_order_for_new_user(self, new_user_with_accesstoken):
        token = new_user_with_accesstoken['token']
        order_ingredients = {
            'ingredients': [Constants.HASH_INGREDIENT_FLUO_BUN, Constants.HASH_INGREDIENT_MEAT_MOLLUSC]}
        response = requests.post(Constants.CREATING_ORDER_URL, json=order_ingredients,
                      headers={'Authorization': token}, timeout=30)
        print(response.status_code)
        print(response.json())




