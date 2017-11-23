from model.group import Group
from random import randrange


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    index = randrange(len(old_groups))
    group = Group(name="new group1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(header="new header"))
#    app.group.modify_first_group(Group(header="new header1"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
