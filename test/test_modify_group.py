def test_test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group()
    app.session.logout()