import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators.constants import Constants
import requests

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator, delay_time):
        return WebDriverWait(self.driver, delay_time).until(EC.visibility_of_element_located(locator),
                                                            message=f'Not found {locator}')
    def find_element_presented(self, locator, delay_time):
        return WebDriverWait(self.driver, delay_time).until(EC.presence_of_element_located(locator),
                                                            message=f'Not found {locator}')

    def scroll_to_element_located(self, driver, locator, delay_time):
        element = self.find_element_located(locator, delay_time)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, delay_time).until(EC.visibility_of_element_located(locator),
                                                            message=f'Not found {locator}')

    def click_on_element_located(self, locator, delay_time):
        element = self.find_element_located(locator, delay_time)
        element.click()



    def get_text_from_element_located(self, locator):
        return self.find_element_located(locator, delay_time=5).text

    def set_text_to_element_located(self, locator, text, delay_time):
        element = self.find_element_located(locator, delay_time)
        return element.send_keys(text)

    def drag_and_drop_element(self, element_from, element_to, delay_time):
        from_element = self.find_element_located(element_from, delay_time=10)
        to_element = self.find_element_located(element_to, delay_time)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    def registration_of_new_user(self, new_user):
        #Регистрация нового пользователя. Возвращает dict с email, password, name, accsessToken

        new_user_1 = new_user
        response = requests.post(Constants.REGISTRATION_USER_URL, json=new_user_1)
        time.sleep(30)
        response_1 = response.json()
        response_2 = response_1.values()
        #accessToken = list(response.json().values())[2]
        accessToken = list(response_2)[2]
        new_user_1['token'] = accessToken
        return new_user_1

    def login_of_new_user(self, new_user):
        result = requests.post(Constants.LOGIN_USER_URL, json=new_user)
        print(result.status_code)
        print(result.json())



    def check_exists_by_xpath(self, locator):
        try:
            self.find_element_located(locator, 5)
            result = True
        except Exception:
            result = False
        return result


