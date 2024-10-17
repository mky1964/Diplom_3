
import pytest
from selenium import webdriver
import allure
from constants.constants import Constants
from api import Api




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


@allure.step('new_user_registration_without_order')
@pytest.fixture
def new_user_registration_without_order():
    api_1 = Api()
    new_user_with_accesstoken = api_1.registration_of_new_user()
    yield new_user_with_accesstoken
    api_1.deleting_of_new_user(new_user_with_accesstoken)






