import json
import random

# CONFIG_PATH = "data/_config.json"
config = {
    "1": {
        "easy": {
            "opnum": 2,
            "ops": ["+", "-"],
            "interval": (1, 10)
        },
        "middle": {
            "opnum": 3,
            "ops": ["+", "-"],
            "interval": (1, 10)
        },
        "hard": {
            "opnum": 3,
            "ops": ["+", "-"],
            "interval": (1, 20)
        }
    },
    "2": {
        "easy": {
            "opnum": 3,
            "ops": ["+", "-"],
            "interval": (1, 20)
        },
        "middle": {
            "opnum": 4,
            "ops": ["+", "-"],
            "interval": (1, 30)
        },
        "hard": {
            "opnum": 4,
            "ops": ["+", "-"],
            "interval": (20, 100)
        }
    },
    "3": {
        "easy": {
            "opnum": 4,
            "ops": ["+", "-"],
            "interval": (20, 100)
        },
        "middle": {
            "opnum": 4,
            "ops": ["+", "-", "*"],
            "interval": (1, 100)
        },
        "hard": {
            "opnum": 5,
            "ops": ["+", "-", "*"],
            "interval": (20, 100)
        }
    },
}


def makeoneques(interval: list, ops: list, opnumber: int):
    if (len(interval) != 2):
        raise RuntimeError("interval should be a binary tuple.")
    if (len(ops) == 0):
        raise RuntimeError("ops should be a non-empty list.")
    if (("(" in ops and ")" not in ops) or (")" in ops and "(" not in ops)):
        raise RuntimeError("'(' and ')' should be both in or not in ops.")
    a, b = interval
    if (a >= b):
        raise RuntimeError("a should be less than b.")
    if (a <= 0):
        raise RuntimeError("a should be more than 0.")
    ret = {}
    ret["ops"] = []
    ret["nums"] = []
    ret["string"] = ""
    lp = 0
    rp = 0
    for _ in range(opnumber):
        op_i = random.randint(0, len(ops) - 1)
        op = ops[op_i]
        if (op == ")"):
            raise RuntimeError("')' should not be in the generated ops")
        if (op == '('):
            ret["ops"].append(op)
            ret["ops"].append(")")
        else:
            ret["ops"].append(op)

    for _ in range(opnumber + 1):
        num = random.randint(a, b)
        ret["nums"].append(num)

    for addi in range(opnumber):
        ret["string"] += str(ret["nums"][addi])
        ret["string"] += str(ret["ops"][addi])

    ret["string"] += str(ret["nums"][opnumber])
    ret["result"] = eval(ret["string"])
    return ret


def testmakeoneques():
    print (makeoneques([1, 10], ['+', '-', '*'], 4))
    return 0


def makesuitques(grade: str, number: int, difficulty: str):
    ops = config[grade][difficulty]["ops"]
    interval = config[grade][difficulty]["interval"]
    opnum = config[grade][difficulty]["opnum"]
    ret = []
    for _ in range(number):
        ques = makeoneques(interval, ops, opnum)
        while (ques["result"] < 0 or ques["result"] >= 250):
            ques = makeoneques(interval, ops, opnum)
        ques = cut(ques)
        ret.append(ques)

    ret = {index: ques for (index, ques) in enumerate(ret)}
    return ret


def cut(ques: dict):
    leng = len(ques["nums"])
    cut_i = random.randint(0, leng - 1)
    ques["show_nums"] = {}
    ques["show_nums"] = ques["nums"]
    ques["cutnum"] = ques["nums"][cut_i]
    ques["show_nums"][cut_i] = "__"
    ques["show_string"] = ""
    for addi in range(len(ques["ops"])):
        ques["show_string"] += str(ques["show_nums"][addi]) + " "
        ques["show_string"] += str(ques["ops"][addi]) + " "
    ques["show_string"] += str(ques["show_nums"][len(ques["ops"])]) + " = " + str(ques["result"])
    return ques


if __name__ == "__main__":
    ret = makesuitques("1", 100, "easy")
    json.dump(ret, open("test.json", 'w', encoding="utf-8"))
