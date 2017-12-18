from model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="before mod"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "after mod"
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(header="new header"))
#    app.group.modify_first_group(Group(header="new header1"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
