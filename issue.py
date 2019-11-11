from san import*
from function import*
from random import *

def issues(grade,mode):
    r = randint(0, 10)
    #1年级
    if grade=='%E4%B8%80%E5%B9%B4%E7%BA%A7':
        #简单模式
        if mode=='%E7%AE%80%E5%8D%95':
            if r<=7:
                return add_sub_5 ()
            elif r<=9:
                return add_sub_10()
            else :
                return add_sub_20()
        #普通模式
        elif mode=='%E4%B8%AD%E7%AD%89':
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
    elif grade=='%E4%BA%8C%E5%B9%B4%E7%BA%A7':
        #简单模式
        if mode=='%E7%AE%80%E5%8D%95':
            if r<=3:
                return add_sub_100()
            elif r<=7:
                return add_sub_100_3()
            else:
                return mul_biao()
        #普通模式
        elif mode=='%E4%B8%AD%E7%AD%89':
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
                return add_sub_1k ()
    #3年级
    else:
        # 简单模式
        if mode == '%E7%AE%80%E5%8D%95':
            if r <= 2:
                return mix_100_3()
            elif r <= 7:
                return add_sub_1k ()
            else:
                return mul_2_1 ()
        # 普通模式
        elif mode == '%E4%B8%AD%E7%AD%89':
            if r <= 1:
                return add_sub_1k ()
            elif r <= 4:
                return mul_2_1 ()
            elif r <= 7:
                return  mul_2_2 ()
            else:
                return div_3_1 ()
        # 困难模式
        else:
            if r <= 2:
                return mul_2_1 ()
            elif r <= 5:
                return mul_2_2 ()
            elif r <= 9:
                return div_3_1 ()
            else:
                return mix_2()


