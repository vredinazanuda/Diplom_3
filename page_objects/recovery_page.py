import allure
from page_objects.base_page import BasePage
from data import Urls
from locators.recovery_page_locators import RecoveryPageLocators
from data import Credentials
class RecoveryPage(BasePage):

    @allure.step("Ввести значение в поле, нажать кнопку, ожидать загрузки элемента")
    def set_value_click_button_and_wait(self, field_locator, value, button_locator, wait_locator):
        self.set_value(field_locator, value)
        self.click_element(button_locator)
        self.wait_element(wait_locator)

    @allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def open_from_login_page(self):
        self.open_page_and_waiting_element_download(Urls.LOGIN_PAGE,
                                                             RecoveryPageLocators.recovery_password_link)
        self.click_element_and_waiting_element_download(RecoveryPageLocators.recovery_password_link,
                                                                 RecoveryPageLocators.recovery_input_email_field)
    @allure.step('Ввод почты и клик по кнопке «Восстановить»')
    def input_email_and_open_next_page(self):
        self.open_page_and_waiting_element_download(Urls.RECOVERY_INPUT_EMAIL_PAGE,
                                                             RecoveryPageLocators.recovery_input_email_field)
        self.set_value_click_button_and_wait(RecoveryPageLocators.recovery_input_email_field,
                                                      Credentials.EMAIL,
                                                      RecoveryPageLocators.recovery_button,
                                                      RecoveryPageLocators.recovery_input_password_field)

    @allure.step('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_recovery_password_visibility(self):
        self.open_page_and_waiting_element_download(Urls.RECOVERY_INPUT_EMAIL_PAGE,
                                                             RecoveryPageLocators.recovery_input_email_field)
        self.set_value_click_button_and_wait(RecoveryPageLocators.recovery_input_email_field,
                                                      Credentials.EMAIL,
                                                      RecoveryPageLocators.recovery_button,
                                                      RecoveryPageLocators.recovery_input_password_field)
        self.set_value_click_button_and_wait(RecoveryPageLocators.recovery_input_password_field,
                                                      Credentials.PASSWORD,
                                                      RecoveryPageLocators.recovery_input_password_visibility_button,
                                                      RecoveryPageLocators.recovery_input_visible_password_field)