import allure
from conftest import driver
from conftest import random_user_data
from conftest import random_user_register
from conftest import random_user_login
from conftest import random_user_delete
from page_objects.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from data import Urls


class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    @allure.description('Открыть страницу авторизации. Кликнуть по кнопке "Конструктор". Проверить, что url изменился'
                        'и соответсвует главной странице')
    def test_main_page_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_waiting_element_download(Urls.LOGIN_PAGE, BasePageLocators.constructor_button)
        main_page.click_element_and_waiting_element_download(BasePageLocators.constructor_button,
                                                             MainPageLocators.constructor_header)

        assert main_page.get_url() == Urls.MAIN_PAGE


    @allure.title('Переход по клику на "Лента заказов"')
    @allure.description('Кликнуть по кнопке "Лента заказов". Проверить, что url изменился и соответствует странице'
                        'с лентой заказов')
    def test_main_page_open_feed(self, driver):
        main_page = MainPage(driver)
        main_page.wait_element(BasePageLocators.feed_button)
        main_page.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             MainPageLocators.feed_header)

        assert main_page.get_url() == Urls.FEED_PAGE


    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Кликнуть по карточке ингредиента. Проверить, что изменился url страницы и в нем добавился '
                        'идентификатор ингредиента')
    def test_main_page_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.wait_element(MainPageLocators.constructor_header)
        main_page.scroll_page(MainPageLocators.ingredient_filling_link)
        main_page.click_element_and_waiting_element_download(MainPageLocators.ingredient_filling_link,
                                                             MainPageLocators.modal_header)

        assert main_page.get_url() == Urls.INGREDIENT_PAGE


    @allure.title('Всплывающее окно с деталями ингредиента закрывается кликом по крестику,')
    @allure.description('Кликнуть по карточке ингредиента, в модальном окне кликнуть крестик. Проверить, что модальное'
                        'окно закрылось отсутствием локатора указывающего на открытую секцию в модальном окне')
    def test_main_page_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.wait_element(MainPageLocators.constructor_header)
        main_page.scroll_page(MainPageLocators.ingredient_filling_link)
        main_page.click_element_and_waiting_element_download(MainPageLocators.ingredient_filling_link,
                                                             MainPageLocators.modal_opened_section)
        main_page.click_element_and_waiting_element_download(MainPageLocators.modal_close_button,
                                                             MainPageLocators.constructor_header)

        assert not main_page.is_elements_exist(MainPageLocators.modal_opened_section)


    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('Запомнить счетчик ингредиента до добавления в заказ. Добавить ингредиент в заказ. Проверить, '
                        'что счетчик ингредиента увеличился сравнениием значений счетчика до и после добавления.')
    def test_main_page_basket_counter_growth(self, driver):
        main_page = MainPage(driver)
        counter_before = main_page.counter_value(MainPageLocators.ingredient_filling_counter)
        main_page.add_ingredient_to_basket(MainPageLocators.ingredient_filling_link)
        counter_after = main_page.counter_value(MainPageLocators.ingredient_filling_counter)

        assert counter_before < counter_after


    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Запомнить значение номера заказа в невидимом модальном окне. Добавить несколько ингредиентов '
                        'в заказ. Кликнуть кнопку оформления заказа. Проверить что модальное окно стало видимым и '
                        'номер заказа изменился')
    def test_main_page_place_order_authorized_success(self, driver, random_user_data, random_user_register,
                                                      random_user_login, random_user_delete):
        main_page = MainPage(driver)
        order_id_before = main_page.text_element(MainPageLocators.order_id)
        main_page.add_ingredient_to_basket(MainPageLocators.ingredient_bun_link)
        main_page.add_ingredient_to_basket(MainPageLocators.ingredient_filling_link)
        main_page.click_element_and_waiting_element_download(MainPageLocators.basket_button,
                                                             MainPageLocators.order_id)
        order_id_after = main_page.text_element(MainPageLocators.order_id)

        assert order_id_after != order_id_before and main_page.is_elements_exist(MainPageLocators.modal_opened_section)
