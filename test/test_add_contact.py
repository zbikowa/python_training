#-*- coding: utf-8 -*-
from model.contact import Contact
from sys import maxsize


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Jan", lastname="Piotr", address="Komornicza 10", email="agnieszka@agnieszka.pl")
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
