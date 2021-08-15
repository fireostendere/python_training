from model.group import Group


def test_mod_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first(Group(name="mod_group", header="mod_group", footer="mod_group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)