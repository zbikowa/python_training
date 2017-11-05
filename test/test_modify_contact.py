def test_test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact()
    app.session.logout()