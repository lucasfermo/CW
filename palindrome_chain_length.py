import math,os, sys,random,time,turtle,operator
import datetime


def palindrome_chain_length(n):
    count=0
    found=False

    while not found:
        m=int(str(n)[::-1])
        if m==n:
            return count
        n=m+n
        tmp=int(str(n)[::-1])
        if tmp==n or m<10:
            found=True
        count+=1
    return count


print(palindrome_chain_length(6))
