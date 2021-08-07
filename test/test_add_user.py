# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.user.create(User(firstname="test", middlename="test", lastname="test", nickname="test"))
