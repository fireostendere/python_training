
from model.contact import Contact


def test_check_all_contact(app, db):
    all_contact_main_page = app.contact.get_contact_list()
    all_contact_db = db.get_contact_list()
    assert sorted(all_contact_main_page, key=Contact.id_or_max) == sorted(all_contact_db, key=Contact.id_or_max)