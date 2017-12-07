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


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    #assert len(old_contact) + 1 == len(new_contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
