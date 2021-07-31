# -*- coding: utf-8 -*-
from model.user import User





def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User(firstname="test", middlename="test", lastname="test", nickname="test"))
    app.session.logout()