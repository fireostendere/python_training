# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    old_users = app.user.get_user_list()
    user = User(firstname="test", middlename="test", lastname="test", nickname="test")
    app.user.create(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)