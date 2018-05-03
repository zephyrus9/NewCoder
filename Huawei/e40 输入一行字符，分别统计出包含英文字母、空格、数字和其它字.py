# -*-coding: utf-8 -*-
# Author:

def num_count(s):
    a = [0,0,0,0]
    for i in s:
        if i.isalpha():
            a[0] += 1
        elif i.isspace():
            a[1] += 1
        elif i.isdigit():
            a[2] += 1
        else:
            a[3] += 1
    for i in a:
        print(i)

while True:
    try:
        num_count(input())
    except Exception as e:
        break
