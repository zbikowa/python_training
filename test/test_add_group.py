# -*- coding: utf-8 -*-
from python_training.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="234", header="234", footer="2344"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
