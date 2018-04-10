# -*-coding: utf-8 -*-
# Author: 
while True:
    try:
        s = input()
        l = list(reversed(s))
        # print(l)
        res = []
        for i in l:
            res.append(i)
        print(''.join(res))
    except:
        break