
class GroupHelper:
    def __init__(self,app):
        self.app = app

    def open_gruops_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def return_to_gruops_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group1):
        driver = self.app.driver
        # открытие вкладки группы
        self.open_gruops_page()
        # добавление новой группы
        driver.find_element_by_name("new").click()
        self.fill_group_form(group1)
        # добавление группы
        driver.find_element_by_name("submit").click()
        # возврат на вкладку грппы
        self.return_to_gruops_page()

    def change_field_value(self, field_value,text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_value).click()
            driver.find_element_by_name(field_value).clear()
            driver.find_element_by_name(field_value).send_keys(text)

    def fill_group_form(self, group):
        driver = self.app.driver
        # заполнение формы группы
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def delete_first_group(self):
        driver = self.app.driver
        # открытие вкладки группы
        self.open_gruops_page()
        #выбрать группу певрую
        self.select_first_group()
        # кликнуть удалить
        driver.find_element_by_name("delete").click()
        self.return_to_gruops_page()

    def modify_first_group(self,new_group_data):
        driver = self.app.driver
        self.open_gruops_page()
        # выбрать группу певрую
        self.select_first_group()
        # открыть группу на редактирвоание
        driver.find_element_by_name("edit").click()
        #заполнить форму
        self.fill_group_form(new_group_data)
        #нажать на кнопку обновить
        driver.find_element_by_name("update").click()
        # возврат на вкладку грппы
        self.return_to_gruops_page()

    def select_first_group(self):
        # выбрать группу певрую (отдельный метод)
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def count(self):
        driver = self.app.driver
        self.open_gruops_page()
        return len(driver.find_elements_by_name("selected[]"))

