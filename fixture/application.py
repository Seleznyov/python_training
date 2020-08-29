from selenium import webdriver
from python_traning.fixture.session import SessionHelper
class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session=SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_gruops_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def return_to_gruops_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def create_gruop(self,group):
        driver = self.driver
        # открытие вкладки группы
        self.open_gruops_page()
        # добавление новой группы
        driver.find_element_by_name("new").click()
        # заполнение формы группы
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # добавление группы
        driver.find_element_by_name("submit").click()
        # возврат на вкладку грппы
        self.return_to_gruops_page()

    def destroy(self):
        self.driver.quit()