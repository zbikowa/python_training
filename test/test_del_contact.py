from python_training.model.contact import Contact


def test_delete_first_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(name="test",middlename="ew", lastname="noe", nickname="zbik", title="jh",
                                   company="kj", address="jkh", home="dfs", mobile="fds", email="fd", byear="fds"))
    app.contact.delete_first_contact()
