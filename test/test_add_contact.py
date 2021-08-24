# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_email(maxlen, postfix):
    symbols = string.ascii_lowercase
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + postfix


def random_number(maxlen):
    return [random.choice(string.digits) for i in range(random.randrange(maxlen))]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="",
                    homephone="", mobilephone="",
                    workphone="", secondaryphone="",
                    email="", email2="", email3="", address="")] + [
               Contact(firstname=random_string("firstname", 15), lastname=random_string("lastname", 5),
                       homephone=random_number(15), mobilephone=random_number(15), workphone=random_number(15),
                       secondaryphone=random_number(15),
                       email=random_email(10, "mail.ru"), email2=random_email(10, "rambler.ru"),
                       email3=random_email(10, "google.com"),
                       address=random_string("address", 15))
               for i in range(2)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
