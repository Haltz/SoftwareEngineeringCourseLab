from random import *
import datetime
mitime=datetime.datetime.now().microsecond
seed(mitime)  #以当前时间的毫秒为种子

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
    if pos==0:
        return{'sk':'__ x '+str(second)+' = '+str(first*second),'ak':str(first)}
    elif pos==1:
        return {'sk': str(first)+' x __ = ' + str(first * second), 'ak': str(second)}
    else:
        return {'sk':str(first)+' x '+str(second)+' = __','ak':str(first*second)}

# 口诀表内除法
def div_biao():
    first = randint(1, 9)
    second = randint(1, 9)
    pos=randint(0,2)
    if pos==0:
        return {'sk':'__ ÷ '+str(first)+' = '+str(second),'ak':str(first*second)}
    elif pos==1:
        return {'sk': str(first * second) + ' ÷ __ =' + str(second) ,'ak': str(first)}
    else:
        return {'sk': str(first * second) + ' ÷ ' + str(first) + ' = __', 'ak': str(second)}

#有余数除
def div_remainder():
    first = randint(2, 9)
    second = randint(1, 9)
    remainder = randint(0,first-1)
    pos=randint(0,3)
    if pos==0:
        return {'sk':'__ ÷ '+str(first)+' = '+str(second)+' 余 '+str(remainder),'ak':str(first*second)}
    elif pos==1:
        return{'sk':str(first*second)+' ÷ __='+str(second)+' 余 '+str(remainder),'ak':str(first)}
    elif pos==2:
        return{'sk':str(first*second)+' ÷ '+str(first)+' = __ 余 '+str(remainder),'ak':str(second)}
    else:
        return{'sk':str(first*second)+' ÷ '+str(first)+' = '+str(second)+' 余 __','ak':str(remainder)}

#100以内加减乘除混合（3位数）
def mix_100_3():
    op1=randint(0,3)
    op2 = randint(0, 3)
    while(((op1==2)&(op2==2))|((op1==2)&(op2==3))|((op1==3)&(op2==3))):
        op2 = randint(0, 3)
    pos=randint(0,3)
    if op1==0:
        if op2==0:
            first=randint(0,99)
            second = randint(0,99)
            third =randint(0,99)
            mins=min(first,second,third)
            sums=sum([first,second,third])
            maxs=max(first,second,third)
            mids=sums-maxs-mins
            if pos == 0:
                return {'sk': '__ + ' + str(mids - mins) + ' + ' + str(maxs - mids) + ' = ' + str(maxs),
                        'ak': str(mins)}
            elif pos == 1:
                return {'sk': str(mins) + ' + __ + ' + str(maxs - mids) + ' = ' + str(maxs),
                        'ak': str(mids - mins)}
            elif pos == 2:
                return {'sk': str(mins) + ' + ' + str(mids - mins) + ' + __ = ' + str(maxs),
                        'ak': str(maxs - mids)}
            else:
                return {'sk': str(mins) + ' + ' + str(mids - mins) + ' + ' + str(mids - mins) + ' = __',
                        'ak': str(maxs)}
        elif op2==1:
            first = randint(0, 99)
            second = randint(0, 99)
            third = randint(0, 99)
            mins = min(first, second, third)
            sums = sum([first, second, third])
            maxs = max(first, second, third)
            if pos==0:
                return {'sk': '__ + ' + str(sums - maxs -  mins) + ' - ' + str(mins) + ' = ' + str(maxs-mins),
                        'ak': str(2*maxs+mins-sums)}
            elif pos==1:
                return {'sk': str(2*maxs+mins-sums) +' + __ - ' + str(mins) + ' = ' + str(maxs-mins),
                        'ak': str(sums - maxs -  mins)}
            elif pos==2:
                return {'sk': str(2*maxs+mins-sums) +' + ' + str(sums - maxs -  mins) + ' - __ = ' + str(maxs-mins),
                        'ak': str(mins)}
            else:
                return {'sk': str(2*maxs+mins-sums) + ' + ' + str(sums - maxs -  mins) + ' - '+ str(mins) + ' = __' ,
                        'ak': str(maxs-mins)}
        elif op2==2:
            second=randint(1,9)
            third=randint(1,9)
            first=randint(0,99-second-third)
            if pos == 0:
                return {'sk': '__ + ' + str(second) + ' x ' + str(third) + ' = ' + str(first+second*third),
                        'ak': str(first)}
            elif pos == 1:
                return {'sk': str(first) + ' + __ x ' + str(third) + ' = ' + str(first+second*third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first) + ' + ' + str(second) + ' x __ = ' + str(first+second*third),
                        'ak': str(third)}
            else:
                return {'sk': str(first) + ' + ' + str(second) + ' x ' + str(third) + ' = __',
                        'ak': str(first+second*third)}
        else:
            second = randint(1, 9)
            third = randint(1, 9)
            first = randint(0, 99 - second )
            if pos == 0:
                return {'sk': '__ + ' + str(second*third) + ' ÷ ' + str(third) + ' = ' + str(first+second),
                        'ak': str(first)}
            elif pos == 1:
                return {'sk': str(first) + ' + __ ÷ ' + str(third) + ' = ' + str(first+second),
                        'ak': str(second*third)}
            elif pos == 2:
                return {'sk': str(first) + ' + ' + str(second*third) + ' ÷ __ = ' + str(first+second),
                        'ak': str(third)}
            else:
                return {'sk': str(first) + ' + ' + str(second*third) + ' ÷ ' + str(third) + ' = __',
                        'ak': str(first+second)}
    elif op1==1:
        if op2==0:
            first=randint(0,99)
            second=randint(0,99)
            third=randint(0,99-max(first,second,0)+min(first,second,99))
            maxs=max(first,second)
            mins=min(first,second)
            if pos == 0:
                return {'sk': '__ - ' + str(mins) + ' + ' + str(third) + ' = ' + str(maxs-mins+third),
                        'ak': str(maxs)}
            elif pos == 1:
                return {'sk': str(maxs) + ' - __ + ' + str(third) + ' = ' + str(maxs-mins+third),
                        'ak': str(mins)}
            elif pos == 2:
                return {'sk': str(maxs) + ' - ' + str(mins) + ' + __ = ' + str(maxs-mins+third),
                        'ak': str(third)}
            else:
                return {'sk': str(maxs) + ' - ' + str(mins) + ' + ' + str(third) + ' = __',
                        'ak': str(maxs-mins+third)}
        elif op2==1:
            first=randint(0,99)
            second=randint(0,99)
            third=randint(0,99)
            maxs=max(first,second,third)
            mins=min(first,second,third)
            sums=sum([first,second,third])
            if pos == 0:
                return {'sk': '__ - ' + str(2*maxs-sums+mins) + ' - ' + str(sums-maxs-2*mins) + ' = ' + str(mins + third),
                        'ak': str(maxs)}
            elif pos == 1:
                return {'sk': str(maxs) + ' - __ - ' + str(third) + ' = ' + str(mins + third),
                        'ak': str(2*maxs-sums+mins)}
            elif pos == 2:
                return {'sk': str(maxs) + ' - ' + str(2*maxs-sums+mins) + ' - __ = ' + str(mins + third),
                        'ak': str(sums-maxs-2*mins)}
            else:
                return {'sk': str(maxs) + ' - ' + str(2*maxs-sums+mins) + ' - ' + str(sums-maxs-2*mins) + ' = __',
                        'ak': str(mins + third)}
        elif op2==2:
            second=randint(1,9)
            third=randint(1,9)
            first=randint(second*third,99)
            if pos == 0:
                return {'sk': '__ - ' + str(second) + ' x ' + str(third) + ' = ' + str(first-second*third),
                        'ak': str(first)}
            elif pos == 1:
                return {'sk': str(first) + ' - __ x ' + str(third) + ' = ' + str(first-second*third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first) + ' - ' + str(second) + ' x __ = ' + str(first-second*third),
                        'ak': str(third)}
            else:
                return {'sk': str(first) + ' - ' + str(second) + ' x ' + str(third) + ' = __',
                        'ak': str(first-second*third)}
        else:
            second = randint(1, 9)
            third = randint(1, 9)
            first = randint(second, 99)
            if pos == 0:
                return {'sk': '__ - ' + str(second*third) + ' ÷ ' + str(third) + ' = ' + str(first-second),
                        'ak': str(first)}
            elif pos == 1:
                return {'sk': str(first) + ' - __ ÷ ' + str(third) + ' = ' + str(first-second),
                        'ak': str(second*third)}
            elif pos == 2:
                return {'sk': str(first) + ' - ' + str(second*third) + ' ÷ __ = ' + str(first-second),
                        'ak': str(third)}
            else:
                return {'sk': str(first) + ' - ' + str(second*third) + ' ÷ ' + str(third) + ' = __',
                        'ak': str(first-second)}
    elif op1==2:
        if op2==0:
            first=randint(1,9)
            second=randint(1,9)
            third=randint(0,99-first*second)
            if pos == 0:
                return {'sk': '__ x ' + str(second) + ' + ' + str(third) + ' = ' + str(first *second+third),
                        'ak': str(first)}
            elif pos == 1:
                return {'sk': str(first) + ' x __ + ' + str(third) + ' = ' + str(first *second+third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first) + ' x ' + str(second) + ' + __ = ' + str(first *second+third),
                        'ak': str(third)}
            else:
                return {'sk': str(first) + ' x ' + str(second) + ' + ' + str(third) + ' = __',
                        'ak': str(first *second+third)}
        else:
            first = randint(1, 9)
            second = randint(1, 9)
            third = randint(0, first * second)
            if pos == 0:
                return {'sk': '__ x ' + str(second) + ' - ' + str(third) + ' = ' + str(first *second-third),
                        'ak': str(first)}
            elif pos == 1:
                return {'sk': str(first) + ' x __ - ' + str(third) + ' = ' + str(first *second-third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first) + ' x ' + str(second) + ' - __ = ' + str(first *second-third),
                        'ak': str(third)}
            else:
                return {'sk': str(first) + ' x ' + str(second) + ' - ' + str(third) + ' = __',
                        'ak': str(first *second-third)}
    else:
        if op2==0:
            first = randint(1, 9)
            second = randint(1, 9)
            third = randint(0, 99-first)
            if pos == 0:
                return {'sk': '__ ÷ ' + str(second) + ' + ' + str(third) + ' = ' + str(first+third),
                        'ak': str(first*second)}
            elif pos == 1:
                return {'sk': str(first*second) + ' ÷ __ + ' + str(third) + ' = ' + str(first+third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first*second) + ' ÷ ' + str(second) + ' + __ = ' + str(first+third),
                        'ak': str(third)}
            else:
                return {'sk': str(first*second) + ' ÷ ' + str(second) + ' + ' + str(third) + ' = __',
                        'ak': str(first+third)}
        elif op2==1:
            first = randint(1, 9)
            second = randint(1, 9)
            third = randint(0, first)
            if pos == 0:
                return {'sk': '__ ÷ ' + str(second) + ' - ' + str(third) + ' = ' + str(first - third),
                        'ak': str(first * second)}
            elif pos == 1:
                return {'sk': str(first * second) + ' ÷ __ - ' + str(third) + ' = ' + str(first - third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first * second) + ' ÷ ' + str(second) + ' - __ = ' + str(first - third),
                        'ak': str(third)}
            else:
                return {'sk': str(first * second) + ' ÷ ' + str(second) + ' - ' + str(third) + ' = __',
                        'ak': str(first - third)}
        else:
            first = randint(1, 9)
            second = randint(1, 9)
            third = randint(1,9)
            if pos == 0:
                return {'sk': '__ ÷ ' + str(second) + ' x ' + str(third) + ' = ' + str(first * third),
                        'ak': str(first * second)}
            elif pos == 1:
                return {'sk': str(first * second) + ' ÷ __ x ' + str(third) + ' = ' + str(first * third),
                        'ak': str(second)}
            elif pos == 2:
                return {'sk': str(first * second) + ' ÷ ' + str(second) + ' x __ = ' + str(first * third),
                        'ak': str(third)}
            else:
                return {'sk': str(first * second) + ' ÷ ' + str(second) + ' x ' + str(third) + ' = __',
                        'ak': str(first * third)}







