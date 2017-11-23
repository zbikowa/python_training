from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count():
        app.contact.create(Contact(firstname="new contact", middlename="new"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="changed name", middlename="bew")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
