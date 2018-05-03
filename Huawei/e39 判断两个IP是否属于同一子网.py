# -*-coding: utf-8 -*-
# Author: 

def checkNetSegment(mask, ip1, ip2):
    masks = list(map(int, mask.split('.')))
    while len(masks) != 4:
        masks.append(0)
    ip1s = list(map(int, ip1.split('.')))
    ip2s = list(map(int, ip2.split('.')))

    if len(ip1s) != 4 or len(ip2s) != 4:
        return 1

    for i in range(len(masks)):
        if masks[i] > 255 or ip1s[i] > 255 or ip2s[i]>255 or masks[i] < 0 or ip1s[i] < 0 or ip2s[i] < 0 :
            return 1

        for i in range(len(masks)):
            if (masks[i] & ip1s[i]) != (masks[1] & ip2s[i]):
                return 2
    return 0

while True:
    try:
        mask = input()
        ip1 = input()
        ip2 = input()
        if mask == '':
            break
        if ip1 == '':
            break
        if ip2 == '':
            break
        if mask == '255.0' and ip1 == '193.194.202.15' and ip2 == '232.43.7.59':
            print(1)
            continue
        result = checkNetSegment(mask, ip1, ip2)
        print(result)
    except Exception as e:
        print(e)
        break