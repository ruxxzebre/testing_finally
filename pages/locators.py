from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocarors():
    LOGIN = (By.CLASS_NAME, 'login_form')
    REGISTER = (By.CLASS_NAME, 'register_form')