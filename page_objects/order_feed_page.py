import allure

import locators.order_feed_page_locators
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Urls


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение заказа в ленте заказов по номеру")
    def is_displayed_order_in_feed(self, order_number):
        order_locator = [By.XPATH,
                         locators.order_feed_page_locators.OrderFeedPageLocators.order_feed_locator_form.format(order_number=order_number)]
        return self.is_elements_exist(order_locator)


    @allure.step("Проверить отображение заказа в истории заказов по номеру")
    def is_displayed_order_in_history(self, order_number):
        order_locator = [By.XPATH,
                         locators.order_feed_page_locators.OrderFeedPageLocators.order_history_locator_form.format(order_number=order_number)]
        return self.is_elements_exist(order_locator)


    @allure.step("Проверить отображение заказа в списке заказов в работе по номеру")
    def is_displayed_order_in_status_box_in_process(self, order_number):
        order_locator = self.order_number_in_in_process_box_element(order_number)
        return self.is_elements_exist(order_locator)


    @staticmethod
    @allure.step("Получить элемент с номером заказа из списке готовых заказов")
    def order_number_in_ready_box_element(order_number):
        element = [By.XPATH,
                   locators.order_feed_page_locators.OrderFeedPageLocators.order_list_locator_form.format(order_number=order_number)]
        return element


    @staticmethod
    @allure.step("Получить элемент с номером заказа из списка заказов в работе")
    def order_number_in_in_process_box_element(order_number):
        element = [By.XPATH,
                   locators.order_feed_page_locators.OrderFeedPageLocators.order_list_ready_locator_form.format(order_number=order_number)]
        return element


    @allure.step("Ожидание появления заказа в списке")
    def wait_order_in_box(self, locator):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def feed_page_open_order(self):
        self.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             OrderFeedPageLocators.top_order)
        top_order_in_feed = self.text_element(OrderFeedPageLocators.top_order_number_in_feed)
        self.click_element_and_waiting_element_download(OrderFeedPageLocators.top_order,
                                                             OrderFeedPageLocators.modal_opened_section)
        order_in_modal = self.text_element(OrderFeedPageLocators.order_number_in_modal)
        return top_order_in_feed, order_in_modal

    @allure.step('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def feed_order_in_history_exists_in_feed(self):
        order_number = self.place_order_get_number(MainPageLocators.ingredient_bun_link,
                                                        MainPageLocators.ingredient_filling_link)
        self.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             OrderFeedPageLocators.top_order)
        is_order_in_feed = self.is_displayed_order_in_feed(order_number)
        self.click_element_and_waiting_element_download(BasePageLocators.account_button,
                                                             AccountPageLocators.order_history_button)
        self.click_element_and_waiting_element_download(AccountPageLocators.order_history_button,
                                                             AccountPageLocators.order_history_list)
        is_order_in_history = self.is_displayed_order_in_history(order_number)
        return is_order_in_feed, is_order_in_history

    @allure.step('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    def feed_page_counters_growth(self, counter):
        self.click_element_and_waiting_element_download(BasePageLocators.feed_button, counter)
        counter_before = self.text_element(counter)
        self.open_page_and_waiting_element_download(Urls.MAIN_PAGE, MainPageLocators.ingredient_bun_link)
        order_number = self.place_order_get_number(MainPageLocators.ingredient_bun_link,
                                                        MainPageLocators.ingredient_filling_link)
        self.click_element_and_waiting_element_download(BasePageLocators.feed_button, counter)
        self.wait_element(OrderFeedPageLocators.status_box)
        order_number_in_in_process_box = OrderFeedPage.order_number_in_in_process_box_element(order_number)
        self.wait_order_in_box(order_number_in_in_process_box)
        order_number_in_ready_box = OrderFeedPage.order_number_in_ready_box_element(order_number)
        self.wait_order_in_box(order_number_in_ready_box)
        counter_after = self.text_element(counter)
        return counter_after, counter_before

    @allure.step('После оформления заказа его номер появляется в разделе В работе.')
    def feed_page_order_number_in_status_box(self):
        order_number = self.place_order_get_number(MainPageLocators.ingredient_bun_link,
                                                        MainPageLocators.ingredient_filling_link)
        self.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             OrderFeedPageLocators.status_box)
        order_number_in_in_process_box = OrderFeedPage.order_number_in_in_process_box_element(order_number)
        self.wait_order_in_box(order_number_in_in_process_box)
        return order_number