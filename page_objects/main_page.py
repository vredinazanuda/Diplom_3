import allure

from locators.base_page_locators import BasePageLocators
from page_objects.base_page import BasePage
from data import Urls
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Получить значение счетчика")
    def counter_value(self, ingredient):
        self.scroll_page(ingredient)
        counter = self.text_element(ingredient)
        return counter


    @allure.step('Переход по клику на "Конструктор"')
    def page_open_constructor(self):
        self.open_page_and_waiting_element_download(Urls.LOGIN_PAGE, BasePageLocators.constructor_button)
        self.click_element_and_waiting_element_download(BasePageLocators.constructor_button,
                                                             MainPageLocators.constructor_header)

    @allure.step('Переход по клику на "Лента заказов"')
    def page_open_feed(self):
        self.wait_element(BasePageLocators.feed_button)
        self.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             MainPageLocators.feed_header)

    @allure.step('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def page_ingredient_details_modal(self):
        self.wait_element(MainPageLocators.constructor_header)
        self.scroll_page(MainPageLocators.ingredient_filling_link)
        self.click_element_and_waiting_element_download(MainPageLocators.ingredient_filling_link,
                                                             MainPageLocators.modal_header)

    @allure.step('Всплывающее окно с деталями ингредиента закрывается кликом по крестику,')
    def page_ingredient_modal_close(self):
        self.wait_element(MainPageLocators.constructor_header)
        self.scroll_page(MainPageLocators.ingredient_filling_link)
        self.click_element_and_waiting_element_download(MainPageLocators.ingredient_filling_link,
                                                             MainPageLocators.modal_opened_section)
        self.click_element_and_waiting_element_download(MainPageLocators.modal_close_button,
                                                             MainPageLocators.constructor_header)

    @allure.step('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def page_basket_counter_growth(self):
        counter_before = self.counter_value(MainPageLocators.ingredient_filling_counter)
        self.add_ingredient_to_basket(MainPageLocators.ingredient_filling_link)
        counter_after = self.counter_value(MainPageLocators.ingredient_filling_counter)
        return counter_before, counter_after

    @allure.step('Залогиненный пользователь может оформить заказ')
    def page_place_order_authorized_success(self):
        order_id_before = self.text_element(MainPageLocators.order_id)
        self.add_ingredient_to_basket(MainPageLocators.ingredient_bun_link)
        self.add_ingredient_to_basket(MainPageLocators.ingredient_filling_link)
        self.click_element_and_waiting_element_download(MainPageLocators.basket_button,
                                                             MainPageLocators.order_id)
        order_id_after = self.text_element(MainPageLocators.order_id)
        return order_id_before, order_id_after

    @allure.step('Проверка всплывающего окна с деталями ингредиента')
    def check_page_ingredient_modal_close(self):
        return self.is_elements_exist(MainPageLocators.modal_opened_section)