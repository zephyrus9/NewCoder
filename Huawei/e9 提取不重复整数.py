# -*-coding: utf-8 -*-
# Author: 
while True:
    try:
        s = input()
        l = list(reversed(s))
        res = []
        for i in l:
            if i not in res:
                res.append(i)
        print(''.join(res))

    except:
        break