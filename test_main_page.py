from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from time import sleep
from .links import link_selpyaw as link, link_loginreg as link_logreg
import pytest

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link, timeout=2)
    page.open()
    page.should_be_login_link()

def test_should_be_login_page(browser):
    page = LoginPage(browser, link_logreg)
    page.open()
    page.should_be_login_page()