import allure
from page_objects.base_page import BasePage


class RecoveryPage(BasePage):

    @allure.step("Ввести значение в поле, нажать кнопку, ожидать загрузки элемента")
    def set_value_click_button_and_wait(self, field_locator, value, button_locator, wait_locator):
        self.set_value(field_locator, value)
        self.click_element(button_locator)
        self.wait_element(wait_locator)
