# -*-coding: utf-8 -*-
# Author:


def separateStr(s):
    if len(s) <= 8:
        print(s + '0'*(8 - len(s)))
    else:
        # while len(s) > 8:
        #     print(s[:8])
        #     s = s[8:]
        # print(s + '0'*(8 - len(a)))
        print(s[:8])
        return separateStr(s[8:])

a = input()
b = input()
separateStr(a)
separateStr(b)
