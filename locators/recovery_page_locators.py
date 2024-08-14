from selenium.webdriver.common.by import By


class RecoveryPageLocators:

    recovery_password_link = [By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"]
    recovery_password_link_class = [By.CLASS_NAME, "Auth_link__1fOlj"]
    recovery_input_email_field = [By.XPATH,".//label[text()='Email']/../input[@type='text' and @name='name']"]
    recovery_button = [By.XPATH, ".//button[text()='Восстановить']"]
    recovery_input_password_field = [By.XPATH, ".//label[text()='Пароль']/../"
                                               "input[@type='password' and @name='Введите новый пароль']"]
    recovery_input_visible_password_field = [By.XPATH, ".//label[text()='Пароль']/../"
                                             "input[@type='text' and @name='Введите новый пароль']"]
    recovery_input_password_visibility_button = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]
