# -*-coding: utf-8 -*-
# Author:
import sys

def check_ip(ip):
    if len(ip) != 4 and '' in ip:
        return False
    else:
        try:
            for i in range(4):
                if int(ip[i]) < 0 or int(ip[i]) > 255:
                    return False
            else:
                return True
        except:
            return False

def check_mask(mask):
    sub = ['254', '252','248', '240', '224', '192', '128', '0']
    if len(mask) != 4:
        return False
    if mask[0] == '255':
        if mask[1] == '255':
            if mask[2] == '255':
                if mask[3] in sub:
                    return True
                else:
                    return False
            elif mask[2] in sub and mask[3] == '0':
                return True
            else:
                return False
        elif mask[1] in sub and mask[2] == mask[3] =='0':
            return True
        else:
            return False
    elif mask[0] in sub and mask[1] == mask[2] == mask[3] == '0':
        return True
    else:
        return False

typeA = 0
typeB = 0
typeC = 0
typeD = 0
typeE = 0
errorIP = 0
privIP = 0

while True:
    string = sys.stdin.readline().strip()
    if string == "":
        break
    ip = string.split("~")[0].split(".")
    mask = string.split("~")[1].split(".")
    # print(ip, mask)
    if check_ip(ip) and check_mask(mask):
        if 1 <= int(ip[0]) <= 126:
            typeA += 1
        if 128 <= int(ip[0]) <= 191:
            typeB += 1
        if 192 <= int(ip[0]) <= 223:
            typeC += 1
        if 224 <= int(ip[0]) <= 239:
            typeD += 1
        if 240 <= int(ip[0]) <= 255:
            typeE += 1
        if int(ip[0]) == 10 or (int(ip[0]) == 172 and 16 <= int(ip[1]) <= 31) or (int(ip[0]) == 192 and int(ip[1]) == 168):
            privIP += 1
        # print(ip)
    else:
        errorIP += 1
        # print(errorIP)
print("%s %s %s %s %s %s %s" %(typeA,typeB,typeC,typeD,typeE,errorIP,privIP))
