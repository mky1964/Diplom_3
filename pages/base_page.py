import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


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
        WebDriverWait(self.driver, delay_time).until(EC.element_to_be_clickable(locator))
        element = self.find_element_located(locator, delay_time)
        element.click()

    @allure.step('get_text_from_element_located')
    def get_text_from_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.find_element_located(locator, delay_time=10).text

    @allure.step('set_text_to_element_located')
    def set_text_to_element_located(self, locator, text, delay_time):
        element = self.find_element_located(locator, delay_time)
        return element.send_keys(text)

    @allure.step('drag_and_drop_element')
    def drag_and_drop_element(self, element_from, element_to, delay_time):
        from_element = self.find_element_located(element_from, delay_time)
        to_element = self.find_element_located(element_to, delay_time)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()



    @allure.step('check_exists_by_xpath')
    def check_exists_by_xpath(self, locator):
        try:
            self.find_element_located(locator, 5)
            result = True
        except Exception:
            result = False
        return result



    @allure.step('wait_of_vanishing_of_overlay_base')
    def wait_of_vanishing_of_overlay_base(self, overlay_locator, delay_time):  #Ожидание пропадания всплывающего объекта
        WebDriverWait(self.driver, delay_time).until_not(EC.visibility_of_element_located(overlay_locator))


    @allure.step('format_locator')
    def format_locator(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)





