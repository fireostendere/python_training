# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php?selected%5B%5D=1&delete=Delete+group%28s%29")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test_group")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test_group")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test_group")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")





    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
