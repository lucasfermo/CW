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

def trib(signature,n):
    final=[]
    for i in range(n):
        try:
            final.append(signature[i])
        except:
            pass
    for i in range(2,n-1):
        temp=signature[i]+signature[i-1]+signature[i-2]
        signature.append(temp)
        final.append(temp)
    return final

print(trib([0.5,0.5,0.5],10))
