# -*-coding: utf-8 -*-
# Author: 
"""题目描述
编写”长整数相乘”程序，实现两个任意长度的长整数(正数)相乘，输出结果.

输入描述:
第一行输入数字A的字符串，字符范围（0～9），第二行输入数字B的字符串，字符范围（0～9）。
输出描述:
输出A、B俩数相乘的结果，结果为字符串。"""

import operator
a = int(input().strip())
b = int(input().strip())

print(str(a*b))