from model.contact import Contact
import random


def test_delete_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test", address="fgd", email="agnieszka@agnieszka.pl",
                                   homephone="34242", mobilephone="3244", workphone="34245", secondaryphone="334234"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


