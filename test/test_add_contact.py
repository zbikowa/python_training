#-*- coding: utf-8 -*-
from model.contact import Contact
import random
import string

#
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])
#
#
# def random_number(prefix, maxlen):
#     numbers = string.digits*10
#     return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


def test_add_contact(app, json_contact):
    fixture_contact = json_contact
    old_contacts = app.contact.get_contact_list()
    app.contact.create(fixture_contact)
    #assert len(old_contact) + 1 == len(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts.append(fixture_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
