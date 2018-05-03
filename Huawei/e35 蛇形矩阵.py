# -*-coding: utf-8 -*-
# Author: 
while True:
    try:
        n = int(input().strip())
        res = [[0 for i in range(0)] for j in range(n)]
        k = 1
        for i in range(n):
            for j in range(i+1):
                res[i-j].append(str(k))
                k += 1
        print(res)
        for i in range(n):
            print(' '.join(res[i]))
    except:
        break