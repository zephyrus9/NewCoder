# -*-coding: utf-8 -*-
# Author:

def sort_lst(l):
    res = []
    odd = []
    even = []
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(l[i])
        else:
            odd.append(l[i])
    even = sorted(even)
    odd = sorted(odd)
    if len(l)%2 == 0:
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
    else:
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        res.append(even[-1])
    return ''.join(res)

def convert(lst):
    res = ''
    for i in lst:
        if '0'<=i<='9' or 'a'<=i<='f' or 'A'<=i<='F':
            tmp = bin(int(i, 16))[2:]
            tmp = (4 - len(tmp)) * '0' + tmp
            s = (hex(int(tmp[::-1],2))[2:]).upper()
        else:
            s = i
        res += s
    return res

while True:
    try:
        l1, l2 = input().split()
        l = list(l1) + list(l2)
        print(convert(sort_lst(l)))
    except:
        break

