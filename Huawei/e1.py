# -*-coding: utf-8 -*-
# Author:

import sys

l = sys.stdin.readline().strip()
# 工作数量N
N = int(l.split()[0])
# 小伙伴数量
M = int(l.split()[1])
s = []
for i in range(N):
    line = list(sys.stdin.readline().split())
    s[i] = line
ability = sys.stdin.readline().split()

