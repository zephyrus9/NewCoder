# -*-coding: utf-8 -*-
# Author: 

def bottle(num):
    num = int(num)
    if num == 0 or num == 1:
        return 0
    elif num ==2:
        return 1
    else:
        return num // 3 + bottle(num//3 + num % 3)

while True:
    try:
        num = input()
        print(bottle(num))
    except:
        break