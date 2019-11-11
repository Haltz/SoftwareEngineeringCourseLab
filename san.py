from random import *
#1000以内加减法(含负数) 返回值:{sk:式子显示的字符串,ak:答案字符}
def add_sub_1k () :
    first = randint(1, 1000)
    second = randint(1, 1000)
    op = randint(0, 2)  # 判断是加法还是减法,0是加法，1是减法
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空,2是第三个空
    while (first + second > 1000) or (first + second < -1000) or (first - second > 1000) or (first - second < -1000):
        first = randint(1, 1000)
        second = randint(1, 1000)
    if op == 0:
        ans = first + second
        if pos == 0:
            want = str(first)
            str_ = "__" + "+" + str(second) + "=" + str(ans)
        elif pos == 1:
            want = str(second)
            str_ = str(first) + "+" + "__" + "=" + str(ans)
        else:
            want = str(ans)
            str_ = str(first) + "+" + str(second) + "=" + "__"
    else:
        ans = first - second
        if pos == 0:
            want = str(first)
            str_ = "__" + "-" + str(second) + "=" + str(ans)
        elif pos == 1:
            want = str(second)
            str_ = str(first) + "-" + "__" + "=" + str(ans)
        else:
            want = str(ans)
            str_ = str(first) + "-" + str(second) + "=" + "__"
    return{"sk": str_, "ak": want}

#2位乘1位 返回值:{sk:式子显示的字符串,ak:答案字符}
def mul_2_1 ():
    first = randint(0, 9)
    second = randint(10, 99)
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空,2是第三个空
    ans = first * second
    if pos == 0:
        want = str(first)
        str_ = "__" + "*" + str(second) + "=" + str(ans)
    elif pos == 1:
        want = str(second)
        str_ = str(first) + "*" + "__" + "=" + str(ans)
    else:
        want = str(ans)
        str_ = str(first) + "*" + str(second) + "=" + "__"
    return{"sk": str_, "ak": want}

#2位乘2位 返回值:{sk:式子显示的字符串,ak:答案字符}
def mul_2_2 ():
    first = randint(10, 99)
    second = randint(10, 99)
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空,2是第三个空
    ans = first * second
    if pos == 0:
        want = str(first)
        str_ = "__" + "*" + str(second) + "=" + str(ans)
    elif pos == 1:
        want = str(second)
        str_ = str(first) + "*" + "__" + "=" + str(ans)
    else:
        want = str(ans)
        str_ = str(first) + "*" + str(second) + "=" + "__"
    return{"sk": str_, "ak": want}

#3位除以1位 返回值:{sk:式子显示的字符串,ak:答案字符}
def div_3_1 ():
    a1 = randint(100, 999)
    a2 = randint(1, 9)
    b1 = randint(10, 99)
    b2 = randint(1, 9)
    c1 = randint(10, 99)
    c2 = randint(10, 99)
    chp = randint(0, 2)
    if chp == 0:
        while a1*a2 > 999 :
            a1 = randint(100, 999)
            a2 = randint(1, 9)
        first = a1 * a2
        second = a1
    elif chp == 1:
        while b1*b2 > 999 or b1*b2<100:
            b1 = randint(10, 99)
            b2 = randint(1, 9)
        first = b1 * b2
        #second = random.choice((b1, b2))
        second = b2
    else:
        while c1 * c2 > 999 or c1 * c2 < 100:
            c1 = randint(10, 99)
            c2 = randint(10, 99)
        first = c1 * c2
        #second = random.choice((c1, c2))
        second = c1
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空,2是第三个空
    ans = first / second
    if pos == 0:
        want = str(first)
        str_ = "__" + "÷" + str(second) + "=" + str(ans)
    elif pos == 1:
        want = str(second)
        str_ = str(first) + "÷" + "__" + "=" + str(ans)
    else:
        want = str(ans)
        str_ = str(first) + "÷" + str(second) + "=" + "__"
    return{"sk": str_, "ak": want}

#3个数的混合四则运算 返回值:{sk:式子显示的字符串,ak:答案字符}
def mix_2():
    first = randint(10, 99)
    second = randint(10, 99)
    third = randint(10, 99)
    chp = randint(0, 5) # 运算符号
    if chp == 0:
        ans = first + second - third
        want = str(ans)
        str_ = str(first) + "+" + str(second) + "-" + str(third) + "=" + "__"
    elif chp == 1:
        ans = first * (second + third)
        want = str(ans)
        str_ = str(first) + "*" + "(" + str(second) + "+" + str(third) + ")" + "=" + "__"
    elif chp == 2:
        ans = (first - second) * third
        want = str(ans)
        str_ = "(" + str(first) + "-" + str(second) + ")" + "*" + str(third) + "=" + "__"
    elif chp == 3:
        ans = first - second + third
        want = str(ans)
        str_ = str(first) + "-" + str(second) + "+" + str(third) + "=" + "__"
    elif chp == 4:
        ans = first * (second - third)
        want = str(ans)
        str_ = str(first) + "*" + "(" + str(second) + "-" + str(third) + ")" + "=" + "__"
    else:
        ans = (first - second) * third
        want = str(ans)
        str_ = "(" + str(first) + "-" + str(second) + ")" + "*" + str(third) + "=" + "__"
    return{"sk": str_, "ak": want}