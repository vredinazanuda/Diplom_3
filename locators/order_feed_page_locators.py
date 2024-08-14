from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    top_order = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a"]
    modal_opened_section = [By.XPATH, ".//section[contains(@class, 'modal_opened')]"]
    order_number_in_modal = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                             "div[contains(@class, 'Modal_modal__contentBox')]/"
                             "p[contains(@class, 'text_type_digits-default')]"]
    top_order_number_in_feed = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]//"
                                          "div[contains(@class, 'OrderHistory_textBox')]/"
                                          "p[contains(@class, 'text_type_digits-default')]"]

    number_in_new_order_modal = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                                           "div[contains(@class, 'Modal_modal__contentBox')]/"
                                           "h2[contains(@class, 'text_type_digits-large')]"]
    ready_animation = [By.XPATH, ".//img[@src='./static/media/tick.887b83be.gif']"]

    counter_all_time = [By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number')]"]
    counter_today = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number')]"]
    status_box = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]"]
