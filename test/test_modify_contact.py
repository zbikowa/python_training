from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="new contact", lastname="new"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="changed name", lastname="bew", address="poznanska 10", email="agnieszka@agnieszka.pl")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
