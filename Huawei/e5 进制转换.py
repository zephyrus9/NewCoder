# -*-coding: utf-8 -*-
# Author:

# 输入一个十六进制的数值字符串。
# int()的用法：int(x, base=n), 将base进制的x转换成十进制形式。
# x 必须是字符形式的，
# 否则：TypeError: int() can't convert non-string with explicit base

while True:
    try:
        n = input()
        print(int(n, 16))
    except:
        break

