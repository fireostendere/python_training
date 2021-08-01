def test_delete_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.delete_first()
    app.session.logout()
