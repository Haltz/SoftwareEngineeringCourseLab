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

#10以内加减法含0 返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果,'pos':挖空的位置}
def add_sub_10():
    first = randint(0, 9)
    second = randint(0, 9)
    while (first == second):
        second = randint(0, 9)
    op = randint(0, 1)  # 判断是加法还是减法,0是加法，1是减法
    pos = randint(0,2)   #判断挖哪个空，0是第一个空，1是第二个空
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

#20以内加法 返回值:{'fir':第一个运算数,'sec':第二个运算数,'res':运算结果}
def add_20() :
    first=randint(0,19)
    second=randint(0,19)
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空
    while (first==second):
        second=randint(0,19)
    if first > second:
        return{'fir':second,'sec':(first-second),'res':first,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，res表示运算结果
    else:
        return{'fir':first,'sec':(second-first),'res':second,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数

#20以内加减法含0 返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_20() :
    first=randint(0,19)
    second=randint(0,19)
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空
    while (first==second):
        second=randint(0,19)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second),'pos':pos}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first),'pos':pos}

#100以内加减法2位数（直接求结果）返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_100() :
    first=randint(0,99)
    second=randint(0,99)
    while (first==second):
        second=randint(0,99)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空
    if first > second:
        if op == 0:
            return{'fir':second,'sec':(first-second),'op':op,'res':first,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符,res表示运算结果
        else:
            return{'fir':first,'sec':second,'op':op,'res':(first-second),'pos':pos}
    else:
        if op == 0:
            return{'fir':first,'sec':(second-first),'op':op,'res':second,'pos':pos}   #fir表示第一个运算数，sec表示第二个运算数，op表示运算符
        else:
            return{'fir':second,'sec':first,'op':op,'res':(second-first),'pos':pos}

#100以内加减法3位数 返回值:{'fir':第一个运算数,'sec':第二个运算数,'op':运算符,'res':运算结果}
def add_sub_100_3() :
    first=randint(0,100)
    second=randint(0,100)
    third = randint(0, 100)
    while (first==second):
        second=randint(0,100)
    op1 = randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    op2 = randint(0, 1)
    pos = randint(0, 3)  # 判断挖哪个空，0是第一个空，1是第二个空
    if op1==0:
        if op2==0:
            if first>second:
                while(first==third):
                    third = randint(0, 100)
                if first>third:
                    return {'fir': second, 'sec': (first - second),'trd': (first - third), 'op1': op1, 'op2': op2,'res': first,'pos':pos}
                else:
                    return {'fir': second, 'sec': (first - second), 'trd': (third-first), 'op1': op1, 'op2': op2,
                            'res':third,'pos':pos}
            else:
                while (second == third):
                    third = randint(0, 100)
                if second > third:
                    return {'fir': first, 'sec': (second-first), 'trd': (second - third), 'op1': op1, 'op2': op2,
                            'res': second,'pos':pos}
                else:
                    return {'fir': first, 'sec': (second-first), 'trd': (third - second), 'op1': op1, 'op2': op2,
                            'res': third,'pos':pos}
        else:
            if first>second:
                while(first<=third):
                    third = randint(0, 100)
                    return {'fir': second, 'sec': (first - second),'trd': third, 'op1': op1, 'op2': op2,'res': (first-third),'pos':pos}
            else:
                while (second <= third):
                    third = randint(0, 100)
                    return {'fir': first, 'sec': (second-first), 'trd': third, 'op1': op1, 'op2': op2,
                            'res': (second-third),'pos':pos}
    else:
        if op2==0:
            if first>second:
                while((second+third)>=100):
                    third = randint(0, 100)
                    return {'fir': first, 'sec': (first - second),'trd': third, 'op1': op1, 'op2': op2,'res': second+third,'pos':pos}
            else:
                while ((first+third)>=100):
                    third = randint(0, 100)
                    return {'fir': second, 'sec': (second-first), 'trd':third , 'op1': op1, 'op2': op2,
                            'res': (third+first),'pos':pos}
        else:
            if first>second:
                while(second<=third):
                    third = randint(0, 100)
                    return {'fir': first, 'sec': second,'trd': third, 'op1': op1, 'op2': op2,'res': (first-third-second),'pos':pos}
            else:
                while (first <= third):
                    third = randint(0, 100)
                    return {'fir': second, 'sec': first, 'trd': third, 'op1': op1, 'op2': op2,
                            'res': (second-third-first),'pos':pos}

#口诀表内乘法
def mul_biao():
    first = randint(1, 9)
    second = randint(1, 9)
    pos=randint(0,2)
    return {'fir':second,'sec':first,'op':2,'res':(first*second),'pos':pos}

#口诀表内除法
def div_biao():
    first = randint(1, 9)
    second = randint(1, 9)
    pos=randint(0,2)
    return {'fir':(first*second),'sec':first,'op':2,'res':second,'pos':pos}

#有余数除
def div_remainder():
    first = randint(2, 9)
    second = randint(1, 9)
    remainder = randint(1,first-1)
    pos=randint(0,3)
    return {'fir':(first*second),'sec':first,'op':3,'res':second,'remainder':remainder,'pos':pos}

#100以内加减乘除混合（3位数）
def mix_100_3():
    op1=randint(0,3)
    op2=randint(0,3)
    pos=randint(0,3)
    if op1==0:
        if op2==0:
            first=randint(0,99)
            second = randint(0,99)
            third =randint(0,99)
            mins=min(first,second,third)
            sums=sum([first,second,third])
            maxs=max(first,second,third)
            return{'fir':mins,'sec':sums-maxs-2*mins,'trd':2*maxs+mins-sums,'op1':op1,'op2':op2,'res':maxs,'pos':pos}
        elif op2==1:
            first = randint(0, 99)
            second = randint(0, 99)
            third = randint(0, 99)
            mins = min(first, second, third)
            sums = sum([first, second, third])
            maxs = max(first, second, third)
            return {'fir': 2*maxs+mins-sums, 'sec': sums - maxs -  mins, 'trd':  mins , 'op1': op1, 'op2': op2,
                    'res': maxs-mins, 'pos': pos}
        elif op2==2:
            second=randint(1,9)
            third=randint(1,9)
            first=randint(0,99-second-third)
            return {'fir': first, 'sec': second, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first+second*third, 'pos': pos}
        else:
            second = randint(1, 9)
            third = randint(1, 9)
            first = randint(0, 99 - second )
            return {'fir': first, 'sec': second*third, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first+second, 'pos': pos}
    elif op1==1:
        if op2==0:
            first=randint(0,99)
            second=randint(0,99)
            third=randint(0,99-max(first,second,0)+min(first,second,99))
            return {'fir': max(first,second,0), 'sec': min(first,second,99), 'trd': third, 'op1': op1, 'op2': op2,
                    'res': max(first,second,0)-min(first,second,99)+third, 'pos': pos}
        elif op2==1:
            first=randint(0,99)
            second=randint(0,99)
            third=randint(0,99)
            maxs=max(first,second,third)
            mins=min(first,second,third)
            sums=sum([first,second,third])
            return {'fir': maxs, 'sec': 2*maxs-sums+mins, 'trd': sums-maxs-2*mins, 'op1': op1, 'op2': op2,
                    'res': mins + third, 'pos': pos}
        elif op2==2:
            second=randint(1,9)
            third=randint(1,9)
            first=randint(second*third,99)
            return {'fir': first, 'sec': second, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first-second*third, 'pos': pos}
        else:
            second = randint(1, 9)
            third = randint(1, 9)
            first = randint(second, 99)
            return {'fir': first, 'sec': second*third, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first - second , 'pos': pos}
    elif op1==2:
        if op2==0:
            first=randint(1,9)
            second=randint(1,9)
            third=randint(0,99-first*second)
            return {'fir': first, 'sec': second, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first *second+third, 'pos': pos}
        elif op2==1:
            first = randint(1, 9)
            second = randint(1, 9)
            third = randint(0, first * second)
            return {'fir': first, 'sec': second, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first * second - third, 'pos': pos}
        elif op2==2:
            first=randint(1,9)
            second=randint(1,9/first)
            third=randint(1,9)
            return {'fir': first, 'sec': second, 'trd': third, 'op1': op1, 'op2': op2,
                    'res': first * second *third, 'pos': pos}
        else:
            first=randint(1,9)
            second=randint(1,9)
            third=randint(1,min(9,first*second,9))







