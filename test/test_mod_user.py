from model.user import User
from random import randrange


def test_mod_user(app):
    old_users = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    index = randrange(len(old_users))
    user = User(firstname="test_mod", middlename="test_mod", lastname="test_mod", nickname="test_mod")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_user_list()
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
