from model.contact import Contact
import random


def test_modify_contact_name(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="new contact", lastname="new"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    contact.firstname = 'contact modified'
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

