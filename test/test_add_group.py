# -*- coding: utf-8 -*-
from python_training.model.group import Group


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="234", header="234", footer="2344"))
    app.session.logout()


def test_test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
