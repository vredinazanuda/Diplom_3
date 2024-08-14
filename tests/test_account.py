import allure
from conftest import driver
from conftest import random_user_data
from conftest import random_user_register
from conftest import random_user_login
from conftest import random_user_delete
from page_objects.account_page import AccountPage
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountPageLocators
from data import Urls


class TestAccount:

    @allure.title('Переход по клику на "Личный кабинет" без авторизации')
    @allure.description('Нажать кнопку "Личный кабинет". Проверить, что текщая страница - страница авторизации')
    def test_account_page_open_not_authorized(self, driver):
        account_page = AccountPage(driver)
        account_page.wait_element(BasePageLocators.account_button)
        account_page.click_element_and_waiting_element_download(BasePageLocators.account_button,
                                                                AccountPageLocators.login_page_header)

        assert account_page.get_url() == Urls.LOGIN_PAGE


    @allure.title('Переход по клику на "Личный кабинет" с авторизацей')
    @allure.description('Нажать кнопку "Личный кабинет". Проверить, что текщая страница - профиль пользователя')
    def test_account_page_open_authorized(self, driver, random_user_data, random_user_register,
                                          random_user_login, random_user_delete):
        account_page = AccountPage(driver)
        account_page.wait_element(BasePageLocators.account_button)
        account_page.click_element_and_waiting_element_download(BasePageLocators.account_button,
                                                                AccountPageLocators.order_history_button)

        assert account_page.get_url() == Urls.PROFILE_PAGE


    @allure.title('Переход в раздел "История заказов"')
    @allure.description('Кликнуть кнопку "Личный кабинет", кликнуть "История заказов". Проверить, что текщая страница -'
                        ' страница исотрии заказов')
    def test_account_open_order_history(self, driver, random_user_data, random_user_register,
                                        random_user_login, random_user_delete):
        account_page = AccountPage(driver)
        account_page.two_clicks(BasePageLocators.account_button, AccountPageLocators.order_history_button,
                                AccountPageLocators.order_history_button)

        assert account_page.get_url() == Urls.ORDER_HISTORY_PAGE


    @allure.title('Выход из аккаунта.')
    @allure.description('Кликнуть кнопку "Личный кабинет", кликнуть "Выход". Проверить, что текщая страница -'
                        ' страница авторизации')
    def test_account_logout(self, driver, random_user_data, random_user_register,
                            random_user_login, random_user_delete):
        account_page = AccountPage(driver)
        account_page.two_clicks(BasePageLocators.account_button, AccountPageLocators.logout_button,
                                AccountPageLocators.login_page_header)

        assert account_page.get_url() == Urls.LOGIN_PAGE
