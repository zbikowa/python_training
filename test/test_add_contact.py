#-*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, data_contacts):
    fixture_contact = data_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(fixture_contact)
    new_contact = db.get_contact_list()
    old_contacts.append(fixture_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
