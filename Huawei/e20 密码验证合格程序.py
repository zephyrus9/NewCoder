# -*-coding: utf-8 -*-
# Author:

import sys


def check_psw_num(s):
    a = b = c = d = 0
    for i in s:
        if i.isdigit():
            a = 1
        elif i.isupper():
            b = 1
        elif i.islower():
            c = 1
        else:
            d = 1
    if (a+b+c+d) >= 3:
        return True
    else:
        return False


def check_psw(s):
    for i in range(len(s)-3):
        if s.count(s[i:i+3]) > 1:
            return False
    return True


while True:
    try:
        psw = sys.stdin.readline().strip()
        if psw == '':
            break
        if len(psw) > 8 and check_psw(psw) and check_psw_num(psw):
            print('OK')
        else:
            print('NG')
    except:
        break
""" 测试输入
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
"""