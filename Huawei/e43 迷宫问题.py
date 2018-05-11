# -*-coding: utf-8 -*-
# Author: 
def migong(n,m, l):
    res = [[-1 for i in range(m)] for j in range(n)]
    res[0][0] = 0



n, m = map(int, input().split())
l = [[int(i) for i in input().split()] for j in range(n)]
