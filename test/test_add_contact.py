#-*- coding: utf-8 -*-
from python_training.model.contact import Contact


def test_test_add_contact(app):
    app.contact.create(Contact(name="Jan", middlename="Adam", lastname="Nowak", nickname="jnow", title="mr", company="Intel", address="Starowiejska 10/4", home="400340340", mobile="\\9",
                               email="jan.nowak@gmail.com", byear="1987"))

