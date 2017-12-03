#-*- coding: utf-8 -*-
from model.contact import Contact
from sys import maxsize
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    numbers = string.digits*10
    return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname="", lastname="", address="", email="")] + [
    Contact(firstname=random_string("firstname", 8), lastname=random_string("lastname", 12),
            address=random_string("address", 12), email="agnieszka@agnieszka.pl",
            homephone=random_number("+", 9), mobilephone=random_number("+", 9), workphone=random_number("+", 9),
            secondaryphone=random_number("+", 9))
    for i in range(10)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    #pass
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
