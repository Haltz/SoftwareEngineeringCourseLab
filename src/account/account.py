import json


def signupsave(username, email, passwd):
    json.dump({
        "username": username,
        "email": email,
        "passwd": passwd
    }, open(username + ".json", 'w', encoding='utf8'))


def testsignupsave():
    signupsave('test', 'mail', 'testpasswd')

if __name__ == "__main__":
    testsignupsave()