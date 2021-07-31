# -*- coding: utf-8 -*-
import pytest
from model.user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User(firstname="test", middlename="test", lastname="test", nickname="test"))
    app.session.logout()