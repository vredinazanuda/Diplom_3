import allure

from locators.base_page_locators import BasePageLocators
from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):

    @allure.step("Переход по клику на 'Личный кабинет' без авторизации")
    def page_open_not_authorized(self):
        self.wait_element(BasePageLocators.account_button)
        self.click_element_and_waiting_element_download(BasePageLocators.account_button,
                                                                AccountPageLocators.login_page_header)

    @allure.step("Переход по клику на 'Личный кабинет' c авторизации")
    def page_open_authorized(self):
        self.wait_element(BasePageLocators.account_button)
        self.click_element_and_waiting_element_download(BasePageLocators.account_button,
                                                                AccountPageLocators.order_history_button)

    @allure.step('Переход в раздел "История заказов"')
    def page_open_order_history(self):
        self.two_clicks(BasePageLocators.account_button, AccountPageLocators.order_history_button,
                                AccountPageLocators.order_history_button)

    @allure.step('Выход из аккаунта.')
    def page_logout(self):
        self.two_clicks(BasePageLocators.account_button, AccountPageLocators.logout_button,
                                AccountPageLocators.login_page_header)
