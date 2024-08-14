from selenium.webdriver.common.by import By


class BasePageLocators:

    logo_image = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a[@href='/']"]
    account_button = [By.XPATH,
                      ".//p[contains(@class, 'AppHeader_header__link') and text()='Личный Кабинет']/parent::a"]
    constructor_button = [By.XPATH,
                          ".//p[contains(@class, 'AppHeader_header__link') and text()='Конструктор']/parent::a"]
    feed_button = [By.XPATH,
                   ".//p[contains(@class, 'AppHeader_header__link') and text()='Лента Заказов']/parent::a"]
    basket_button = [By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button"]
    basket_section = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"]
    modal_close_button = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]
    number_in_new_order_modal = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                                           "div[contains(@class, 'Modal_modal__contentBox')]/"
                                           "h2[contains(@class, 'text_type_digits-large')]"]
