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


@allure.step("Запустить браузер. Перейти на главную страницу Stellar Burgers. "
             " Вернуть тип браузера. Закрыть браузер по завершении теста")
@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    browser = None

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

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BasePageLocators.account_button))
    driver.execute_script("arguments[0].click();", driver.find_element(*BasePageLocators.account_button))
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AccountPageLocators.login_field))
    driver.find_element(*AccountPageLocators.login_field).send_keys(random_user_register['email'])
    driver.find_element(*AccountPageLocators.password_field).send_keys(random_user_register['password'])
    driver.execute_script("arguments[0].click();", driver.find_element(*AccountPageLocators.login_button))
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(data.Urls.MAIN_PAGE))


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
