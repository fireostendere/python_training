# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test_group", header="test_group", footer="test_group"))


def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
