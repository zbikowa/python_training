from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count():
        app.contact.create(Contact(firstname="new contact", middlename="new"))
    app.contact.modify_first_contact(Contact(firstname="changed name", middlename="bew"))
