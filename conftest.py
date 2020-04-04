import pytest
from selenium import webdriver

def pytest_addoption(parser):
    # The parameters has default options, such as - default browser is Firefox, and language is english
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption("language")
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        lang = webdriver.FirefoxProfile()
        lang.set_preference("intl.accept_languages", browser_lang)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=lang)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
