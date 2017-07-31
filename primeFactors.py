import math,os, sys,random,time,turtle,operator
import datetime


def primeFactor(n):
    primeString=""
    for i in range(2,n+1):
        if n%i==0:
            found=False
            print(n)
            while not found:
                for j in range(10,0,-1):
                    tmp=i**j
                    if j==1:
                        found=True
                        primeString=primeString+"({})".format(str(i))
                        break
                    elif n%tmp==0:
                        primeString=primeString+"({}**{})".format(str(i),str(j))
                        found=True
                        break
                n=n/tmp
                print(n)

        if n==1:
            return primeString

print(primeFactor(86240))
