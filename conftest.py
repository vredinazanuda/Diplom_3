import allure
import string
import random
import pytest
import requests
import data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountPageLocators
from page_objects import base_page
from page_objects.base_page import BasePage


@allure.step("Запустить браузер. Перейти на главную страницу Stellar Burgers. "
             " Вернуть тип браузера. Закрыть браузер по завершении теста")
#@pytest.fixture(params=['firefox', 'chrome'], scope='function')
@pytest.fixture(params=['chrome'], scope='function')
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.get(data.Urls.MAIN_PAGE)

    yield browser

    browser.quit()


@allure.step("Авторизоваться. Дождаться перехода на главную страницу.")
@pytest.fixture(scope='function')
def random_user_login(driver, random_user_register):
    page = BasePage(driver)
    page.wait_element(BasePageLocators.account_button)
    page.click_element(BasePageLocators.account_button)
    page.wait_element(AccountPageLocators.login_field)
    page.set_value(AccountPageLocators.login_field, random_user_register['email'])
    page.set_value(AccountPageLocators.password_field, random_user_register['password'])
    page.click_element(AccountPageLocators.login_button)
    page.check_url(data.Urls.MAIN_PAGE)

@allure.step("Удалить рандомного пользователя по завершении теста")
@pytest.fixture(scope='function')
def random_user_delete(driver, random_user_register):

    yield

    headers = dict(Authorization=random_user_register['token'])
    wait_ten = 0
    while wait_ten != 10:
        response = requests.delete(data.Urls.USER_AUTHORIZATION_PAGE, headers=headers)
        wait_ten += 1 if response.status_code != 202 else 10


@allure.step('Генерация рандомных учетных данных для регистрации нового пользователя. Вернуть данные.')
@pytest.fixture(scope='function')
def random_user_data():
    letters = string.ascii_lowercase + '1234567890'
    email = ''.join(random.choice(letters) for i in range(15))
    password = ''.join(random.choice(letters) for i in range(15))
    random_body = dict(email=f'{email}@stellarburgers.com', password=password, name='Username')

    return random_body


@allure.step('Зарегистрировать нового рандомного пользователя. Вернуть учетные данные и токен авторизации')
@pytest.fixture(scope='function')
def random_user_register(random_user_data):
    wait_ten = 0
    while wait_ten != 10:
        response = requests.post(data.Urls.USER_REGISTER_PAGE, json=random_user_data)
        wait_ten += 1 if response.status_code != 200 else 10
    random_user_data['token'] = response.json()["accessToken"]

    return random_user_data
