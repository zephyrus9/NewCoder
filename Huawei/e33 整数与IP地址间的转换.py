# -*-coding: utf-8 -*-
# Author: 

# IP转换成数字，将每位IP地址看成256进制；
def ip2num(ip):
    ip = ip.split('.')
    s = sum([256**i * int(j) for i, j in enumerate(ip[::-1])])
    return s

# 将数字转换成IP地址；
def num2ip(num):
    res = []
    bin0 = bin(int(num))[2:]
    if len(bin0) < 32:  # 若二进制位数小于32位，在前边补0；
        bin0 = '0'*(32 - len(bin0)) + bin0
    for i in range(4):
        res.append(str(int(bin0[i*8:(i+1)*8], 2)))
    return '.'.join(res)

while True:
    try:
        ip = input().strip()
        num = input().strip()
        print(ip2num(ip))
        print(num2ip(num))
    except:
        break