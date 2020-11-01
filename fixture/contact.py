from python_traning.model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_value,text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_value).click()
            driver.find_element_by_name(field_value).clear()
            driver.find_element_by_name(field_value).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        # Добавление кэша
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.pen_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_name("input").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

    def opne_contacnt_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.row.find_elements_by_tag_name("a").click()

    def opne_contacnt_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.row.find_elements_by_tag_name("a").click()


