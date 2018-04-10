# -*-coding: utf-8 -*-
# Author: 

while True:
    try:
        num = input()
        s = list(reversed(num))
        # print(s)
        res = []
        for i in s:
            res.append(i)
        # print(res)
        print(''.join(res))
    except:
        break