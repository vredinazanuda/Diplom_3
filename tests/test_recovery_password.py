import allure
import data
from conftest import driver
from data import Urls
from page_objects.recovery_page import RecoveryPage
from locators.recovery_page_locators import RecoveryPageLocators


class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    @allure.description('Открыть страницу авторизации, кликнуть кнопку «Восстановить пароль», '
                        'проверить что текущая страница изменилась на страницу восстановления доступа'
                        ' с эндпоинтом /forgot-password')
    def test_recovery_page_open_from_login_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page_and_waiting_element_download(Urls.LOGIN_PAGE,
                                                             RecoveryPageLocators.recovery_password_link)
        recovery_page.click_element_and_waiting_element_download(RecoveryPageLocators.recovery_password_link,
                                                                 RecoveryPageLocators.recovery_input_email_field)

        assert recovery_page.get_url() == Urls.RECOVERY_INPUT_EMAIL_PAGE


    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Открыть страницу восстановления пароля, ввести значение в поле ввода email и кликнуть '
                        '«Восстановить». Проверить, что текущая страница изменилась на страницу ввода пароля '
                        'с эндпоинтом /reset-password')
    def test_recovery_input_email_and_open_next_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page_and_waiting_element_download(Urls.RECOVERY_INPUT_EMAIL_PAGE,
                                                             RecoveryPageLocators.recovery_input_email_field)
        recovery_page.set_value_click_button_and_wait(RecoveryPageLocators.recovery_input_email_field,
                                                      data.Credentials.EMAIL,
                                                      RecoveryPageLocators.recovery_button,
                                                      RecoveryPageLocators.recovery_input_password_field)

        assert recovery_page.get_url() == Urls.RECOVERY_INPUT_PASSWORD_PAGE


    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    @allure.description('Перейти на страницу востановления пароля, ввести email, кликнуть "Восстановить", на следующей '
                        'странице ввести пароль, нажать кнопку "показать/скрыть пароль". Проверить, что локатора "type"'
                        ' изменил значение на "text"')
    def test_recovery_password_visibility(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page_and_waiting_element_download(Urls.RECOVERY_INPUT_EMAIL_PAGE,
                                                             RecoveryPageLocators.recovery_input_email_field)
        recovery_page.set_value_click_button_and_wait(RecoveryPageLocators.recovery_input_email_field,
                                                      data.Credentials.EMAIL,
                                                      RecoveryPageLocators.recovery_button,
                                                      RecoveryPageLocators.recovery_input_password_field)
        recovery_page.set_value_click_button_and_wait(RecoveryPageLocators.recovery_input_password_field,
                                                      data.Credentials.PASSWORD,
                                                      RecoveryPageLocators.recovery_input_password_visibility_button,
                                                      RecoveryPageLocators.recovery_input_visible_password_field)


        assert recovery_page.get_attribute(RecoveryPageLocators.recovery_input_visible_password_field, 'type') == 'text'
