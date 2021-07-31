# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test_group", header="test_group", footer="test_group"))
    app.session.logout()
    time.sleep(1)


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
