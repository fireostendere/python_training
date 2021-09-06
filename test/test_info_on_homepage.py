
from model.contact import Contact
import re


def test_all_contact_on_home_page(app, db):
    l = len(db.get_contact_list())
    home_page_contact = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(l):
        contact_from_home_page = home_page_contact[i]
        contact_from_db = db.get_contact_list()[i]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_db)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone, contact.workphone,
                                                            contact.secondaryphone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
