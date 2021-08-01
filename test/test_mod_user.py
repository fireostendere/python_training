from model.user import User


def test_mod_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.mod_first(User(firstname="test_mod", middlename="test_mod", lastname="test_mod", nickname="test_mod"))
    app.session.logout()
