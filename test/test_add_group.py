# -*- coding: utf-8 -*-
import pytest
from python_training.model.group import Group
from python_training.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="234", header="234", footer="2344"))
    app.session.logout()


def test_test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
