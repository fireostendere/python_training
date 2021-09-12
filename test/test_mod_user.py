from model.contact import Contact
import random


def test_mod_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="111", lastname="222",
                                   homephone="444", mobilephone="555", workphone="666", secondaryphone="777",
                                   email="888@mail.ru", email2="999@mail.ru", email3="1010@mail.ru", address="1234"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_mod = Contact(firstname="mod", lastname="mod",
                                             homephone="mod", mobilephone="mod", workphone="mod",
                                             secondaryphone="mod",
                                             email="mod", email2="mod",
                                             email3="mod",
                                             address="mod")
    contact_mod.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_mod)
    new_contacts = db.get_contact_list()
    index = 0
    for i in old_contacts:
        if i.id == contact.id:
            old_contacts[index] = contact_mod
            break
        else:
            index = index + 1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)