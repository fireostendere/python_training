
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
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.nickname)
        # submit form
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
