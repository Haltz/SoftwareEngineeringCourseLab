from random import *
import datetime
mitime=datetime.datetime.now().microsecond
random.seed(mitime)  #以当前时间的毫秒为种子

# 5以内加减法不含0 返回值:{'sk':题目,'ak':答案}
def add_sub_5():
    first = randint(1, 5)
    second = randint(1, 5)
    while (first == second):
        second = randint(1, 5)
    op = randint(0, 2)  # 判断是加法还是减法,0是加法，1是减法
    pos = randint(0,2)   #判断挖哪个空，0是第一个空，1是第二个空
    maxs=max(first,second)
    mins=min(first,second)
    if op == 0:
        if pos==0:
            return{'sk':"__ + "+str(maxs-mins)+" = "+str(maxs),'ak':str(mins)}
        elif pos==1:
            return {'sk': str(mins)+" + __ = " + str(maxs), 'ak': str(maxs-mins)}
        else:
            return{'sk':str(mins)+" + "+str(maxs-mins)+" = __",'ak':str(max)}
    else:
        if pos==0:
            return{'sk':"__ - "+str(maxs-mins)+" = "+str(mins),'ak':str(maxs)}
        elif pos==1:
            return{'sk': str(maxs)+" - __ = " + str(mins), 'ak': str(maxs-mins)}
        else:
            return {'sk': str(maxs) + " - " + str(maxs - mins) + " = __", 'ak': str(mins)}

# 10以内加减法含0
def add_sub_10():
    first = randint(0, 9)
    second = randint(0, 9)
    while (first == second):
        second = randint(0, 9)
    op = randint(0, 1)  # 判断是加法还是减法,0是加法，1是减法
    pos = randint(0,2)   #判断挖哪个空，0是第一个空，1是第二个空
    maxs = max(first, second)
    mins = min(first, second)
    if op == 0:
        if pos == 0:
            return {'sk': "__ + " + str(maxs - mins) + " = " + str(maxs), 'ak': str(mins)}
        elif pos == 1:
            return {'sk': str(mins) + " + __ = " + str(maxs), 'ak': str(maxs - mins)}
        else:
            return {'sk': str(mins) + " + " + str(maxs - mins) + " = __", 'ak': str(max)}
    else:
        if pos == 0:
            return {'sk': "__ - " + str(maxs - mins) + " = " + str(mins), 'ak': str(maxs)}
        elif pos == 1:
            return {'sk': str(maxs) + " - __ = " + str(mins), 'ak': str(maxs - mins)}
        else:
            return {'sk': str(maxs) + " - " + str(maxs - mins) + " = __", 'ak': str(mins)}

# 20以内加减法含0
def add_sub_20() :
    first=randint(0,19)
    second=randint(0,19)
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空
    while (first==second):
        second=randint(0,19)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    maxs = max(first, second)
    mins = min(first, second)
    if op == 0:
        if pos == 0:
            return {'sk': "__ + " + str(maxs - mins) + " = " + str(maxs), 'ak': str(mins)}
        elif pos == 1:
            return {'sk': str(mins) + " + __ = " + str(maxs), 'ak': str(maxs - mins)}
        else:
            return {'sk': str(mins) + " + " + str(maxs - mins) + " = __", 'ak': str(max)}
    else:
        if pos == 0:
            return {'sk': "__ - " + str(maxs - mins) + " = " + str(mins), 'ak': str(maxs)}
        elif pos == 1:
            return {'sk': str(maxs) + " - __ = " + str(mins), 'ak': str(maxs - mins)}
        else:
            return {'sk': str(maxs) + " - " + str(maxs - mins) + " = __", 'ak': str(mins)}

# 100以内加减法2位数（直接求结果）
def add_sub_100() :
    first=randint(0,99)
    second=randint(0,99)
    while (first==second):
        second=randint(0,99)
    op=randint(0,1)  #判断是加法还是减法,0是加法，1是减法
    pos = randint(0, 2)  # 判断挖哪个空，0是第一个空，1是第二个空
    maxs = max(first, second)
    mins = min(first, second)
    if op == 0:
        if pos == 0:
            return {'sk': "__ + " + str(maxs - mins) + " = " + str(maxs), 'ak': str(mins)}
        elif pos == 1:
            return {'sk': str(mins) + " + __ = " + str(maxs), 'ak': str(maxs - mins)}
        else:
            return {'sk': str(mins) + " + " + str(maxs - mins) + " = __", 'ak': str(max)}
    else:
        if pos == 0:
            return {'sk': "__ - " + str(maxs - mins) + " = " + str(mins), 'ak': str(maxs)}
        elif pos == 1:
            return {'sk': str(maxs) + " - __ = " + str(mins), 'ak': str(maxs - mins)}
        else:
            return {'sk': str(maxs) + " - " + str(maxs - mins) + " = __", 'ak': str(mins)}

# 100以内加减法3位数
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
            third = randint(0, 100)
            maxs = max(first,second,third)
            mins = min(first,second,third)
            mids = sum([first,second,third])-maxs-mins
            if pos==0:
                return {'sk': '__ + ' + str(mids - mins) + ' + ' + str(maxs - mids) + ' = ' + str(maxs),
                        'ak': str(mins)}
            elif pos==1:
                return {'sk': str(mins) +' + __ + ' + str(maxs - mids) + ' = ' + str(maxs),
                        'ak': str(mids-mins)}
            elif pos==2:
                return {'sk': str(mins) +' + ' + str(mids - mins) + ' + __ = ' + str(maxs),
                        'ak': str(maxs-mids)}
            else:
                return {'sk': str(mins) + ' + ' + str(mids - mins) + ' + '+ str(mids - mins) + ' = __' ,
                        'ak': str(maxs)}
        else:
            while(first<third):
                third = randint(0, 100)
                maxs=max(first,second)
                mins=min(first,second)
            if pos==0:
                return{'sk':'__ + '+str(maxs-mins)+' - '+str(third)+' = '+str(maxs-third),'ak':str(mins)}
            elif pos==1:
                return {'sk': str(mins)+' + __ - ' + str(third) + ' = ' + str(maxs - third),
                        'ak': str(maxs-mins)}
            elif pos==2:
                return {'sk': str(mins)+' + ' + str(maxs - mins) + ' - __ = '  + str(maxs - third),
                        'ak': str(third)}
            else:
                return {'sk': str(mins) + ' + ' + str(maxs-mins) + ' - '+str(third)+' = __',
                        'ak': str(maxs-third)}
    else:
        if op2==0:
            maxs=max(first,second)
            mins=min(first,second)
            while((mins+third)>=100):
                third = randint(0, 100)
            if pos==0:
                return{'sk':'__ - '+str(maxs-mins)+' + '+str(third)+' = '+str(mins+third),'ak':str(maxs)}
            elif pos==1:
                return {'sk': str(maxs)+' - __ + ' + str(third) + ' = ' + str(mins+ third),
                        'ak': str(maxs-mins)}
            elif pos==2:
                return {'sk': str(maxs)+' - ' + str(maxs - mins) + ' + __ = '  + str(mins+ third),
                        'ak': str(third)}
            else:
                return {'sk': str(maxs) + ' - ' + str(maxs-mins) + ' + '+str(third)+' = __',
                        'ak': str(mins+third)}
        else:
            third = randint(0, 100)
            maxs=max(first,second,third)
            mins=min(first,second,third)
            mids=sum([first,second,third])-maxs-mins
            if pos==0:
                return{'sk':'__ - '+str(maxs-mids)+' - '+str(mids-mins)+' = '+str(mins),'ak':str(maxs)}
            elif pos==1:
                return {'sk': str(maxs)+' - __ - ' + str(mids-mins) + ' = ' + str(mins),
                        'ak': str(maxs-mids)}
            elif pos==2:
                return {'sk': str(maxs)+' - ' + str(maxs - mids) + ' - __ = '  + str(mins),
                        'ak': str(mids-mins)}
            else:
                return {'sk': str(maxs) + ' - ' + str(maxs-mids) + ' - '+str(mids-mins)+' = __',
                        'ak': str(mins)}

# 口诀表内乘法
def mul_biao():
    first = randint(1, 9)
    second = randint(1, 9)
    pos=randint(0,2)
    return {'fir':second,'sec':first,'op':2,'res':(first*second),'pos':pos}

# 口诀表内除法
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







