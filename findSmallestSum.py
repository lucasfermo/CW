import math,os, sys,random,time,turtle,operator
import datetime

#Smallest possible sum

def solution(a):
    if len(a)==1:
        return a[0]
    minMod=min(a)
    maxMod=max(a)
    modList=[]
    for i in range(1,25):
        found=True
        for j in a:
            if j%i!=0:
                found=False
        if found:
            modList.append(i)
    return max(modList)*len(a)



print(solution([1,21,55]))
