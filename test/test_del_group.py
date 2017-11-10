from python_training.model.group import Group


def test_delete_first_group(app):
    if not app.group.count():
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
