import math,os, sys,random,time,turtle,operator
import datetime


def scramble(s1,s2):
    required=len(s2)
    count=0
    letterDict={}
    for i in s1:
        if i in letterDict.keys():
            letterDict[i]+=1
        else:
            letterDict[i]=1
    for i in s2:
        if i in letterDict.keys():
            letterDict[i]-=1
            if letterDict[i]<0:
                return False
        else:
            return False
    return True
