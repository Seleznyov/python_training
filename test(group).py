# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from group import Group

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_app(self):
        driver = self.driver
        # отрытие страницы
        self.open_home_page(driver)
        # login
        self.login(driver, username="admin", password="secret")
        # открытие вкладки группы
        self.open_gruops_page(driver)
        # создание новой группы
        self.create_gruop(driver, Group(name="1", header="1", footer="1"))
        # возврат на вкладку грппы
        self.return_to_gruops_page(driver)
        # logout
        self.logout(driver)

    def return_to_gruops_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")

    def create_gruop(self, driver,group):
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

    def open_gruops_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
