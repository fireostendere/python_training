from model.user import User


def test_delete_first_user(app):
    old_user = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    app.user.delete_first()
    assert len(old_user) - 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user[0:1] = []
    assert old_user == new_user