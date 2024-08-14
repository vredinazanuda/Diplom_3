import allure
from page_objects.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Два последовательных клика с ожиданием загрузки элементов")
    def two_clicks(self, locator_1, locator_2, locator_3):
        self.wait_element(locator_1)
        self.click_element(locator_1)
        self.wait_element(locator_2)
        self.click_element(locator_2)
        self.wait_element(locator_3)
