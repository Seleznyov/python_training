
class GroupHelper:
    def __init__(self,app):
        self.app=app

    def open_gruops_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def return_to_gruops_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.driver
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