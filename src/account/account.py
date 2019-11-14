import json
import os
import random

PATH = "data/account"


def signup(username, email, passwd):
    infos = list(os.walk(PATH))
    dirnames = infos[0][1]
    if (username in dirnames):
        return False  # Nor found.
    os.mkdir(PATH + username)
    id = random.randint(100000000000000000, 321282200007020432)
    json.dump({
        "id": id,
        "username": username,
        "email": email,
        "passwd": passwd
    }, open(PATH + username + "/" + username + ".json", 'w', encoding='utf8'))
    json.dump({
        "number": 0,
    }, open(PATH + username + "/" + "tests.json", 'w', encoding='utf8'))
    json.dump({
        "number": 0,
    }, open(PATH + username + "/" + "wrongs.json", 'w', encoding='utf8'))

    return True


def login(username, passwd):
    infos = list(os.walk(PATH))
    print(infos)
    dirnames = infos[0][1]
    if (username not in dirnames):
        return False  # Nor found.
    userpath = PATH + username + "/"
    account = json.load(open(userpath + username + ".json", 'r', encoding="utf-8"))
    if (username == account["username"] and passwd == account["passwd"]):
        return True
    else:
        return False


if __name__ == "__main__":
    print(login("hd", "321282"))
