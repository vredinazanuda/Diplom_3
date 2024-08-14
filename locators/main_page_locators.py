from selenium.webdriver.common.by import By


class MainPageLocators:

    constructor_header = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    feed_header = [By.XPATH, ".//h1[text()='Лента заказов']"]
    ingredient_filling_link = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6e']"]
    ingredient_bun_link = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']"]
    modal_header = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    modal_close_button = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]
    modal_opened_section = [By.XPATH, ".//section[contains(@class, 'modal_opened')]"]
    ingredient_filling_counter = [By.XPATH,
                                  ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6e']//p[contains(@class, 'counter')]"]
    basket_section = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"]
    basket_button = [By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button"]
    order_id = [By.XPATH, ".//p[text()='идентификатор заказа']/../h2"]
