from model.user import User


class UserHelper:
    def __init__(self, app):
        self.app = app

    def open_add_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, user):
        wd = self.app.wd
        # fill form
        self.open_add_user_page()
        self.fill_group_form(user)
        # submit form
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()
        self.user_cache = None

    def fill_group_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first user
        self.select_first_user()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept del
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.user_cache = None

    def select_first_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def mod_first(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_user()
        # submit mod
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill form
        self.fill_group_form(user)
        # submit form
        wd.find_element_by_name("update").click()
        # return to home page
        self.app.open_home_page()
        self.user_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2]
                lastname = cells[1]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.user_cache.append(User(firstname=firstname.text, lastname=lastname.text, id=id))
        return list(self.user_cache)
