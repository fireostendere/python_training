from model.user import User


def test_mod_first_user(app):
        old_users = app.user.get_user_list()
        user = User(firstname="test_mod", middlename="test_mod", lastname="test_mod", nickname="test_mod")
        user.id = old_users[0].id
        app.user.mod_first(user)
        assert len(old_users) == app.user.count()
        new_users = app.user.get_user_list()
        old_users[0] = user
        assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)