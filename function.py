from random import *
import datetime
mitime=datetime.datetime.now().microsecond
random.seed(mitime)  #以当前时间的毫秒为种子

#5以内加减法不含0 返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果,'pos':挖空的位置}
def add_sub_5():
    first = randint(1, 5)
    second = randint(1, 5)
    while (first == second):
        second = randint(1, 5)
    op = randint(0, 2)  # 判断是加法还是减法,0是加法，1是减法
    pos = randint(0,1)   #判断挖哪个空，0是第一个空，1是第二个空
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果,pos是挖的空的位置
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second),'pos':pos}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second,'pos':pos}
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first),'pos':pos}

#10以内加减法含0（直接求结果）返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_10_res() :
    first=randint(0,9)
    second=randint(0,9)
    while (first==second):
        second=randint(0,9)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second)}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first)}

#10以内加减法含0（填运算数） 返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果,'pos':挖空的位置}
def add_sub_10_oper():
    first = randint(0, 9)
    second = randint(0, 9)
    while (first == second):
        second = randint(0, 9)
    op = randint(0, 1)  # 判断是加法还是减法,0是加法，1是减法
    pos = randint(0,1)   #判断挖哪个空，0是第一个空，1是第二个空
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果,pos是挖的空的位置
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second),'pos':pos}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second,'pos':pos}
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first),'pos':pos}

#20以内加法（直接求结果）返回值:{'fir':第一个运算数,'sec':第二个运算数,'res':运算结果}
def add_20_res() :
    first=randint(0,20)
    second=randint(0,20)
    while (first==second):
        second=randint(0,20)
    if first > second:
        return{'fir':second,'sec':(first-second),'res':first}   #fir表示第一个运算数，sec表示第二个运算数，res表示运算结果
    else:
        return{'fir':first,'sec':(second-first),'res':second}   #fir表示第一个运算数，sec表示第二个运算数

#20以内加减法含0（直接求结果）返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_20_res() :
    first=randint(0,20)
    second=randint(0,20)
    while (first==second):
        second=randint(0,20)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second)}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first)}

#100以内加减法2位数（直接求结果）返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_100_res() :
    first=randint(0,100)
    second=randint(0,100)
    while (first==second):
        second=randint(0,100)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second)}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first)}

#100以内加减法3位数（直接求结果）返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_100_res_3() :
    first=randint(0,100)
    second=randint(0,100)
    third = randint(0, 100)
    while (first==second):
        second=randint(0,100)
    op1 = randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    op2 = randint(0, 1)
    if op1==0:
        if op2==0:
            if first>second:
                while(first==third):
                    third = randint(0, 100)
                if first>third:
                    return {'fir': second, 'sec': (first - second),'trd': (first - third), 'op1': op1, 'op2': op2,'res': first}
                else:
                    return {'fir': second, 'sec': (first - second), 'trd': (third-first), 'op1': op1, 'op2': op2,
                            'res':third}
            else:
                while (second == third):
                    third = randint(0, 100)
                if second > third:
                    return {'fir': first, 'sec': (second-first), 'trd': (second - third), 'op1': op1, 'op2': op2,
                            'res': second}
                else:
                    return {'fir': first, 'sec': (second-first), 'trd': (third - second), 'op1': op1, 'op2': op2,
                            'res': third}
        else:
            if first>second:
                while(first<=third):
                    third = randint(0, 100)
                    return {'fir': second, 'sec': (first - second),'trd': third, 'op1': op1, 'op2': op2,'res': (first-third)}
            else:
                while (second <= third):
                    third = randint(0, 100)
                    return {'fir': first, 'sec': (second-first), 'trd': third, 'op1': op1, 'op2': op2,
                            'res': (second-third)}
    else:
        if op2==0:
            if first>second:
                while((second+third)>=100):
                    third = randint(0, 100)
                    return {'fir': first, 'sec': (first - second),'trd': third, 'op1': op1, 'op2': op2,'res': second+third}
            else:
                while ((first+third)>=100):
                    third = randint(0, 100)
                    return {'fir': second, 'sec': (second-first), 'trd':third , 'op1': op1, 'op2': op2,
                            'res': (third+first)}
        else:
            if first>second:
                while(second<=third):
                    third = randint(0, 100)
                    return {'fir': first, 'sec': second,'trd': third, 'op1': op1, 'op2': op2,'res': (first-third-second)}
            else:
                while (first <= third):
                    third = randint(0, 100)
                    return {'fir': second, 'sec': first, 'trd': third, 'op1': op1, 'op2': op2,
                            'res': (second-third-first)}

#口诀表内乘法(直接求结果)
def mul_biao_res():
    first = randint(1, 10)
    second = randint(1, 10)
    return {'fir':second,'sec':first,'op':2,'res':(first*second)}

#口诀表内除法(直接求结果)
def div_biao_res():
    first = randint(1, 10)
    second = randint(1, 10)
    return {'fir':(first*second),'sec':first,'op':2,'res':second}



