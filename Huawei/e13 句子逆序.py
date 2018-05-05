# -*-coding: utf-8 -*-
# Author: 
while True:
    try:
        words = input().split()
        print(' '.join(reversed(words)))
        print(' '.join(words[::-1]))
    except:
        break