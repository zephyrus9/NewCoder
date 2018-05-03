# -*-coding: utf-8 -*-
# Author:
import copy
while True:
    try:
        key = input().strip()
        strings = input().strip()
        l = list("abcdefghijklmnopqrstuvwxyz")
        m = list("abcdefghijklmnopqrstuvwxyz")
        res = []
        for i in list(key):
            if i not in res:
                res.append(i)
        for i in res:
            l.pop(l.index(i))
        ll = res + list(l)
        r = []
        for i in list(strings):
            r.append(ll[m.index(i)])
        print(''.join(r))
    except:
        break
