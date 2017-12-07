# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_group):
    old_groups = app.group.get_group_list()
    app.group.create(json_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(json_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
