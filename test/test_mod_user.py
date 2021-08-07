from model.user import User


def test_mod_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="test"))
    app.user.mod_first(User(firstname="test_mod", middlename="test_mod", lastname="test_mod", nickname="test_mod"))
