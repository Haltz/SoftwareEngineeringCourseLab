import os
import json

PATH = "data/account/"


def get_tests(username):
    userpath = PATH + username + "/"
    tests = json.load(open(userpath + "tests.json", 'r', encoding='utf-8'))
    return tests


def save_tests(username, test: dict):
    tests = json.load(open(PATH + username + "/" + "tests.json", 'r', encoding="utf-8"))
    number = tests["number"]
    tests["number"] = number + 1
    tests["#" + str(number + 1)] = {
        "grade": test["grade"],
        "type": test["type"],
        "difficulty": test["difficulty"],
        "number": test["number"],
        "wrongs": test["wrongs"],
        "accuracy": test["accuracy"],
        "level": test["level"]
    }
    json.dump(tests, open(PATH + username + "/" + "tests.json", 'w', encoding='utf-8'))


def save_wrongs(username, wrongs: dict):
    userpath = PATH + username + "/"
    save = json.load(open(userpath + "wrongs.json", 'r', encoding="utf-8"))
    save["number"] += len(wrongs.keys())
    for key in wrongs.keys():  # key就是题目字符串
        save[key] = {}
        save[key]["wa"] = wrongs[key]["wa"]
        save[key]["ac"] = wrongs[key]["ac"]
        save[key]["grade"] = wrongs[key]["grade"]
        save[key]["type"] = wrongs[key]["type"]
        save[key]["difficulty"] = wrongs[key]["difficulty"]
    json.dump(save, open(userpath + "wrongs.json", 'w', encoding='utf-8'))


def get_wrongs(username):
    userpath = PATH + username + "/"
    wrongs = json.load(open(userpath + "wrongs.json", 'r', encoding="utf-8"))
    return wrongs


def get_account(username):
    userpath = PATH + username + "/" + username + ".json"
    user = json.load(open(userpath, 'r', encoding='utf-8'))
    return user


if __name__ == "__main__":
    test = {
        "id": 1
    }
    save_tests("hd", {})
