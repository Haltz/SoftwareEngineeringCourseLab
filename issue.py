from san import*
from function import*
from random import *

def issues(grade,mode):
    r = randint(0, 10)
    #1年级
    if grade==1:
        #简单模式
        if mode=='easy':
            if r<=7:
                return add_sub_5 ()
            elif r<=9:
                return add_sub_10()
            else :
                return add_sub_20()
        #普通模式
        elif mode=='normal':
            if r<=1:
                return add_sub_5 ()
            elif r<=5:
                return add_sub_10()
            elif r<=8:
                return add_sub_20()
            else:
                return add_sub_100()
        #困难模式
        else:
            if r<=1:
                return add_sub_10()
            elif r<=4:
                return add_sub_20()
            elif r<=8:
                return add_sub_100()
            else:
                return add_sub_100_3()
    #2年级
    elif grade==2:
        #简单模式
        if mode=='easy':
            if r<=3:
                return add_sub_100()
            elif r<=7:
                return add_sub_100_3()
            else:
                return mul_biao()
        #普通模式
        elif mode=='normal':
            if r<=1:
                return add_sub_100_3()
            elif r<=4:
                return mul_biao()
            elif r<=7:
                return div_biao()
            else:
                return div_remainder()
        #困难模式
        else:
            if r<=2:
                return div_biao()
            elif r<=5:
                return div_remainder()
            elif r<=9:
                return mix_100_3()
            else :
                return add_sub_1w ()
    #3年级



