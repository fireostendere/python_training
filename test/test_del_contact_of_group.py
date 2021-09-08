from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_of_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    if len(db.get_contact_list()) == 0:
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="111", lastname="222",
                                       homephone="444", mobilephone="555", workphone="666", secondaryphone="777",
                                       email="888@mail.ru", email2="999@mail.ru", email3="1010@mail.ru",
                                       address="1234"))
    groups_with_contacts = db.get_not_empty_group()
    if len(groups_with_contacts) == 0:
        rand_group = random.choice(db.get_group_list())
        rand_contact = random.choice(db.get_contact_list())
        app.contact.add_to_group_by_id(rand_contact.id, rand_group.name)
        groups_with_contacts = db.get_not_empty_group()
    group = random.choice(groups_with_contacts)
    contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group_by_id(contact.id, group.name)
    contact_in_group = list(db.get_contacts_in_group(Group(id=group.id)))
    assert contact not in contact_in_group