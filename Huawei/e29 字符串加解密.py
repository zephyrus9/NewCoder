# -*-coding: utf-8 -*-
# Author:
dict1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
dict2 = 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA1234567890'

def encryption(lst, d1=dict1, d2=dict2):
    l = []
    for i in list(lst):
        if i in d1:
            l.append(d2[d1.index(i)])
        else:
            l.append(i)
    return ''.join(l)

def decryption(lst, d1=dict2, d2=dict1):
    l = []
    for i in list(lst):
        if i in d1:
            l.append(d2[d1.index(i)])
        else:
            l.append(i)
    return ''.join(l)
while True:
    try:
        l1 = input().strip()
        l2 = input().strip()
        print(encryption(l1))
        print(decryption(l2))
    except:
        break