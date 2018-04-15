# -*-coding: utf-8 -*-
# Author:
from collections import defaultdict

def func(l):
    d = defaultdict(l)
    
while True:
    try:
        l = input().strip()
        print(func(l))
    except:
        break