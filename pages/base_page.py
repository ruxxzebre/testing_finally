
class BasePage():

    def __init__(self, broswer, url):
        self.browser = broswer
        self.url = url

    def open(self):
        self.browser.get(self.url)