from selenium.common.exceptions import NoSuchElementException
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        #if not (wd.current_url.endswith("/index.php") and len(wd.find_element_by_name("home")) > 0):
        #    wd.find_element_by_link_text("home").click()
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        # select modify contact
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        # return to contacts
        self.return_to_contact_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_contact_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        try:
            return len(wd.find_elements_by_name("selected[]"))
        except NoSuchElementException:
            return 0

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                email = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  email=email, all_phones_from_home_page=all_phones
                                                  ))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,  workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, address=address, email=email)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search('H: (.*)', text) .group(1)
        workphone = re.search('W: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        email = re.search('(.*)@(.*).(.*)', text).group(3)
        address = re.search('(.*)\n(.*)(\d)', text).group(3)
        #street_address = re.search('^[a-zA-Z\ ]+[ \t](\d+)', text).group(0)
        #postal_code = re.search('[\d]{2}[-]{1}[\d]{3}', test).group(0)

        return Contact(homephone=homephone,  workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, email=email, address=address)


