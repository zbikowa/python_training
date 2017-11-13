from model.contact import Contact


def test_delete_first_contact(app):
     if not app.contact.count():
         app.contact.create(Contact(firstname="test"))
         app.contact.delete_first_contact()

