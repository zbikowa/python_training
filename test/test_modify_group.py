from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    app.group.modify_first_group(Group(name="new group1"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="new header"))
    app.group.modify_first_group(Group(header="new header1"))
