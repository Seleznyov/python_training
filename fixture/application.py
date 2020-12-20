from selenium import webdriver

from python_traning.fixture.contact import ContactHelper
from python_traning.fixture.session import SessionHelper
from python_traning.fixture.group import GroupHelper

class Application:
    def __init__(self, browser):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Не распознан браузер %s" % browser)
        # self.driver.implicitly_wait(5)            # закомментировал ожидание появления элементов на странице
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            # Скобки не нужны не работал с ними
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()