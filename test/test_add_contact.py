# -*- coding: utf-8 -*-
import pytest
from python_training.model.contact import Contact
from python_training.fixture.application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(name="Jan", middlename="Adam", lastname="Nowak", nickname="jnow", title="mr", company="Intel", address="Starowiejska 10/4", home="400340340", mobile="\\9",
                        email="jan.nowak@gmail.com", byear="1987"))
    app.session.logout()

