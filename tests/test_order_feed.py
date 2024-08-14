import allure
from conftest import driver
from conftest import random_user_data
from conftest import random_user_register
from conftest import random_user_login
from conftest import random_user_delete
import pytest
from page_objects.order_feed_page import OrderFeedPage
from locators.base_page_locators import BasePageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from data import Urls


class TestOrderFeedPage:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Перейти в ленту заказов. Запомнить номер заказа в ленте. Кликнуть по карточке этого заказа. '
                        'Дождаться появления модального окна. Проверить что номер заказа в ленте совпадает с номером '
                        'заказа в модальном окне')
    def test_order_feed_page_open_order(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             OrderFeedPageLocators.top_order)
        top_order_in_feed = feed_page.text_element(OrderFeedPageLocators.top_order_number_in_feed)
        feed_page.click_element_and_waiting_element_download(OrderFeedPageLocators.top_order,
                                                             OrderFeedPageLocators.modal_opened_section)
        order_in_modal = feed_page.text_element(OrderFeedPageLocators.order_number_in_modal)

        assert top_order_in_feed == order_in_modal


    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Создать заказ и запомнить его номер. Перейти в ленту заказов. Сохранить состояние нахождения'
                        ' заказа в ленте true или false. Перейти в профиль, перейти в историю заказов. Сохранить '
                        'состояние нахождения заказа в ленте true или false. Проверить, что оба значения сохраненных '
                        'состояний в значении true, а значит новый заказ отображается и в истории, и в ленте.')
    def test_order_feed_order_in_history_exists_in_feed(self, driver, random_user_data, random_user_register,
                                                        random_user_login, random_user_delete):
        feed_page = OrderFeedPage(driver)
        order_number = feed_page.place_order_get_number(MainPageLocators.ingredient_bun_link,
                                                        MainPageLocators.ingredient_filling_link)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             OrderFeedPageLocators.top_order)
        is_order_in_feed = feed_page.is_displayed_order_in_feed(order_number)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.account_button,
                                                             AccountPageLocators.order_history_button)
        feed_page.click_element_and_waiting_element_download(AccountPageLocators.order_history_button,
                                                             AccountPageLocators.order_history_list)
        is_order_in_history = feed_page.is_displayed_order_in_history(order_number)

        assert is_order_in_feed and is_order_in_history


    @allure.title('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @allure.description('Используя параметризацию запустить тест поочередно для разных счетчиков.'
                        'Перейти в ленту заказов, сохранить значение счетчика. Перейти на главную страницу и создать '
                        'новый заказ. Перейтив ленту заказов. Дождаться появления номера заказов в таблице "В работе".'
                        ' Дождаться появления номера заказа в таблице "Готовы". Сохранить текущее значение счетчика.'
                        'Проверить, что счетчик увеличился сравнением значений счетчика до и после создания заказа.')
    @pytest.mark.parametrize('counter', [OrderFeedPageLocators.counter_all_time,
                                         OrderFeedPageLocators.counter_today])
    def test_order_feed_page_counters_growth(self, driver, random_user_data, random_user_register,
                                             random_user_login, random_user_delete, counter):
        feed_page = OrderFeedPage(driver)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.feed_button, counter)
        counter_before = feed_page.text_element(counter)
        feed_page.open_page_and_waiting_element_download(Urls.MAIN_PAGE, MainPageLocators.ingredient_bun_link)
        order_number = feed_page.place_order_get_number(MainPageLocators.ingredient_bun_link,
                                                        MainPageLocators.ingredient_filling_link)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.feed_button, counter)
        feed_page.wait_element(OrderFeedPageLocators.status_box)
        order_number_in_in_process_box = OrderFeedPage.order_number_in_in_process_box_element(order_number)
        feed_page.wait_order_in_box(order_number_in_in_process_box)
        order_number_in_ready_box = OrderFeedPage.order_number_in_ready_box_element(order_number)
        feed_page.wait_order_in_box(order_number_in_ready_box)
        counter_after = feed_page.text_element(counter)

        assert counter_after > counter_before


    @allure.title('После оформления заказа его номер появляется в разделе В работе.')
    @allure.description('Создать новый заказ, запомнить его номер. Перейти в ленту заказов.'
                        'Сформировать значение элемента с номером  заказа в таблице заказов "В работе". '
                        'Дождаться появления заказа в таблице "В работе"'
                        'Проверить отображение элемента в таблице "В работе"')
    def test_order_feed_page_order_number_in_status_box(self, driver, random_user_data, random_user_register,
                                                        random_user_login, random_user_delete):
        feed_page = OrderFeedPage(driver)
        order_number = feed_page.place_order_get_number(MainPageLocators.ingredient_bun_link,
                                                        MainPageLocators.ingredient_filling_link)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.feed_button,
                                                             OrderFeedPageLocators.status_box)
        order_number_in_in_process_box = OrderFeedPage.order_number_in_in_process_box_element(order_number)
        feed_page.wait_order_in_box(order_number_in_in_process_box)

        assert feed_page.is_displayed_order_in_status_box_in_process(order_number)
