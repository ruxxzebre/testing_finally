from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
#from time import sleep
from .links import link_selpyaw as link
import pytest

def test_adding_to_basket(browser):
    page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear', timeout=10)
    page.open()
    page.add_to_basket()
    __import__('time').sleep(5)