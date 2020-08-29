from selenium import webdriver
class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def login(self, username, password):
        driver = self.driver
        # отрытие страницы
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")

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