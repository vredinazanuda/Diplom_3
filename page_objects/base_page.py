import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step("Открыть страницу")
    def open_page(self, url):
        self.driver.get(url)


    @allure.step("Получить bool если элемент существует")
    def is_enabled_element(self, locator):
        return self.driver.find_element(*locator).is_enabled()


    @allure.step("Получить элемент, если элемент существует")
    def is_elements_exist(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements


    @allure.step("Скроллить странцу до элемента")
    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step("Кликнуть элемент")
    def click_element(self, locator):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*locator))


    @allure.step("Получить текст элемента")
    def text_element(self, locator):
        return self.driver.find_element(*locator).text


    @allure.step("Ожидание появления элемента")
    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))


    @allure.step("Получить адрес текущей страницы")
    def get_url(self):
        return self.driver.current_url


    @allure.step("Ввести значение в поле")
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)


    @allure.step("Получить значение аттрибута элемента")
    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)


    @allure.step("Открыть страницу и ожидать загрузки элемента")
    def open_page_and_waiting_element_download(self, url, locator):
        self.open_page(url)
        self.wait_element(locator)


    @allure.step("Кликнуть по элементу и ожидать загрузки элемента")
    def click_element_and_waiting_element_download(self, click_locator, wait_locator):
        self.click_element(click_locator)
        self.wait_element(wait_locator)


    @allure.step("Добавить ингредиент в корзину")
    def add_ingredient_to_basket(self, ingredient):
        self.scroll_page(ingredient)
        source = self.driver.find_element(*ingredient)
        target = self.driver.find_element(*BasePageLocators.basket_section)
        drag_and_drop(self.driver, source, target)


    @allure.step("Сформировать заказ из двух ингредиентов и передать номер заказа")
    def place_order_get_number(self, first_ingredient, second_ingredient):
        self.add_ingredient_to_basket(first_ingredient)
        self.add_ingredient_to_basket(second_ingredient)
        self.click_element(BasePageLocators.basket_button)
        self.wait_element(BasePageLocators.number_in_new_order_modal)
        while self.text_element(BasePageLocators.number_in_new_order_modal) == '9999':
            pass
        number = self.text_element(BasePageLocators.number_in_new_order_modal)
        self.click_element(BasePageLocators.modal_close_button)
        return number
