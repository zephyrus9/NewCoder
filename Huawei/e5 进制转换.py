# -*-coding: utf-8 -*-
# Author:
# 输入一个十六进制的数值字符串。


while True:
    try:
        n = input()
        print(int(n, 16))
    except:
        break

