import allure
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение заказа в ленте заказов по номеру")
    def is_displayed_order_in_feed(self, order_number):
        order_locator = [By.XPATH, f".//ul[contains(@class, 'OrderFeed_list')]//p[contains(text(), '#0{order_number}')]"]
        return self.is_elements_exist(order_locator)


    @allure.step("Проверить отображение заказа в истории заказов по номеру")
    def is_displayed_order_in_history(self, order_number):
        order_locator = [By.XPATH, f".//ul[contains(@class, 'OrderHistory_profileList')]//"
                                   f"p[contains(text(), '#0{order_number}')]"]
        return self.is_elements_exist(order_locator)


    @allure.step("Проверить отображение заказа в списке заказов в работе по номеру")
    def is_displayed_order_in_status_box_in_process(self, order_number):
        order_locator = self.order_number_in_in_process_box_element(order_number)
        return self.is_elements_exist(order_locator)


    @staticmethod
    @allure.step("Получить элемент с номером заказа из списке готовых заказов")
    def order_number_in_ready_box_element(order_number):
        element = [By.XPATH, f".//ul[contains(@class, 'OrderFeed_orderList_')]/li[text()={order_number}]"]
        return element


    @staticmethod
    @allure.step("Получить элемент с номером заказа из списка заказов в работе")
    def order_number_in_in_process_box_element(order_number):
        element = [By.XPATH, f".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()={order_number}]"]
        return element


    @allure.step("Ожидание появления заказа в списке")
    def wait_order_in_box(self, locator):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(locator))
