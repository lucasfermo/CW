import math,os, sys,random,time,turtle,operator
import datetime

def factorial(n):
    if n==1:
        return n
    if n==0:
        return 0
    if n<0:
        return 0

    return n*factorial(n-1)

def zeros(n):
    f=factorial(n)
    string=str(f)
    if len(string)<2:
        return 0
    zero=True
    count=0
    for i in range(len(string)-1,0,-1):
        if string[i]!="0":
            return count
        count+=1

for i in range(10,100)
