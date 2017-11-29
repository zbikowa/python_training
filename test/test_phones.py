
def test_phones_on_home_pages(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.homephone == contact_from_edit_page.homephone
    assert contact_from_homepage.workphone == contact_from_edit_page.workphone
    assert contact_from_homepage.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_homepage.secondaryphone == contact_from_edit_page.secondaryphone
