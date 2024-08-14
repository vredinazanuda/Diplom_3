from selenium.webdriver.common.by import By


class AccountPageLocators:

    login_page_header = [By.XPATH, ".//div[contains(@class, 'Auth_login')]/h2[text()='Вход']"]
    login_field = [By.XPATH, ".//div[contains(@class, 'Auth_login')]//label[text()='Email']/../input[@name='name']"]
    password_field = [By.XPATH,
                      ".//div[contains(@class, 'Auth_login')]//label[text()='Пароль']/../input[@name='Пароль']"]
    login_button = [By.XPATH, ".//button[text()='Войти']"]
    basket_button = [By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button"]
    order_history_button = [By.XPATH, ".//nav[contains(@class, 'Account_nav')]//a[text()='История заказов']"]
    logout_button = [By.XPATH, ".//nav[contains(@class, 'Account_nav')]//button[text()='Выход']"]
    order_history_list = [By.XPATH,
                          ".//div[contains(@class, 'Account_contentBox')]//ul[contains(@class, 'OrderHistory_list')]"]
    order_history_box = [By.XPATH, ".//div[contains(@class, 'OrderHistory_orderHistory')]"]
