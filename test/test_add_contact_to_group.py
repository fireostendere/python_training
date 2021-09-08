from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="111", lastname="222",
                                   homephone="444", mobilephone="555", workphone="666", secondaryphone="777",
                                   email="888@mail.ru", email2="999@mail.ru", email3="1010@mail.ru", address="1234"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_not_in_group(Group(id=group.id))
    if not contacts:
        app.contact.create(
            Contact(firstname="test", lastname="test", homephone="123", mobilephone="123",
                    workphone="123", secondaryphone="123", address="123",
                    email="123", email2="123", email3="123"))
        contacts = db.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts)
    old_contacts_in_group = list(db.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_to_group_by_id(contact.id, group.name)
    new_contacts_in_group = list(db.get_contacts_in_group(Group(id=group.id)))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    assert contact in new_contacts_in_group
