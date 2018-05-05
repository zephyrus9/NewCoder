# -*-coding: utf-8 -*-
# Author: 

while True:
    try:
        num = input()
        s = list(reversed(num))
        # print(s)
        print(''.join(s))
        # res = []
        # for i in s:
        #     res.append(i)
        # print(''.join(res))
    except:
        break