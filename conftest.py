
from faker import Faker
import pytest
from selenium import webdriver
import allure
from locators.constants import Constants
#import faker



@allure.step('driver')
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    driver.get(Constants.MAIN_PAGE_URL)
    yield driver
    driver.quit()

@allure.step('new_user')
@pytest.fixture
def new_user():

    faker_1 = Faker()
    # генерируем логин, пароль и имя курьера
    email = faker_1.email()
    password = faker_1.password(10)
    name = faker_1.name()
    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    # возвращаем список
    yield payload