# -*-coding: utf-8 -*-
# Author: 
# 找出最长的有效密码串

def longestPalindrome(s):
    if s == s[::-1]:
        return len(s)
    maxlen = 0
    for i in range(len(s)):
        if i-maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
            maxlen += 2
            continue
        if i-maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
            maxlen += 1
    return maxlen

while True:
    try:
        s = input()
        if s:
            print(longestPalindrome(s))
    except:
        break