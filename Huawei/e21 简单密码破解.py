# -*-coding: utf-8 -*-
# Author: 
import sys


def ts(psw):
    l = []
    s = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tvu', 9:'wxyz'}
    for i in list(psw):
        if i.islower():
            for j in s.keys():
                if i in s[j]:
                    l.append(str(j))
                else:
                    pass
        elif i.isupper():
            if i == 'Z':
                l.append('a')
            else:
                l.append(chr(ord(i.lower())+1))
        else:
            l.append(i)
    return ''.join(l)

# 粗暴的方法：
def ts_2(psw):
    l = []
    dict1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    dict2 = 'bcdefghijklmnopqrstuvwxyza22233344455566677778889999'
    for i in list(psw):
        if i in dict1:
            l.append(dict2[dict1.index(i)])
        else:
            l.append(i)
    return ''.join(l)

# for line in sys.stdin.readlines():
line = input()
print(ts_2(line))