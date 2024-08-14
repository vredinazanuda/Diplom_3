import allure
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Получить значение счетчика")
    def counter_value(self, ingredient):
        self.scroll_page(ingredient)
        counter = self.text_element(ingredient)
        return counter


