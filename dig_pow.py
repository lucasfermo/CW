import math,os, sys,random,time,turtle,operator
import datetime


def dig_pow(n,p):
    digits=list(str(n))
    expList=[]
    for i in range(len(digits)):
        expList.append(i+p)
    finalList=[]
    for i in range(len(digits)):
        finalList.append(int(digits[i])**expList[i])
    final=sum(finalList)
    if not final%n:
        return final/n
    else:
        return -1







print(dig_pow(89,1))
