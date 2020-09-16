from selenium import webdriver
from python_traning.fixture.session import SessionHelper
from python_traning.fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(5)             закомментировал ожидание появления элементов на странице
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()