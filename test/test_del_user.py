from model.user import User
from random import randrange


def test_delete_some_user(app):
    old_users = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users[index:index+1] = []
    assert old_users == new_users
