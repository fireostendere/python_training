from model.contact import Contact
import random


def test_mod_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id,
                                     Contact(firstname="mod", lastname="mod",
                                             homephone="mod", mobilephone="mod", workphone="mod",
                                             secondaryphone="mod",
                                             email="mod", email2="mod",
                                             email3="mod",
                                             address="mod"))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(),
                                                                     key=Contact.id_or_max)
