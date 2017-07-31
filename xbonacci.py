import math,os, sys,random,time,turtle,operator
import datetime

#Tribonacci

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def Xbonacci(signature,n):
    fib=len(signature)
    final=signature[:n]
    length=len(final)
    for i in range(n-length):
        temp=0
        for j in range(fib):
            temp+=signature[i+j]
        signature.append(temp)
        final.append(temp)
    return final

print(Xbonacci([0,1],10))
