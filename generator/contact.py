import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n == int(a)
    elif o == "-f":
        f = a


def random_email(maxlen, postfix):
    symbols = string.ascii_lowercase
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + postfix


def random_phone(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="",
                    homephone="", mobilephone="", workphone="",
                    secondaryphone="",
                    email="", email2="",
                    email3="",
                    address="")] + [
               Contact(firstname=random_string("firstname", 15), lastname=random_string("lastname", 5),
                       homephone=random_phone(15), mobilephone=random_phone(15), workphone=random_phone(15),
                       secondaryphone=random_phone(15),
                       email=random_email(10, "mail.ru"), email2=random_email(10, "rambler.ru"),
                       email3=random_email(10, "google.com"),
                       address=random_string("address", 15))
               for i in range(n)
               ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
