import math,os, sys,random,time,turtle,operator
import datetime


def find_Outlier(integers):
    odds=[x for x in integers if x%2!=0]
    evens=[x for x in integers if x%2==0]

    return odds[0] if len(odds)<len(evens) else evens[0]

print(find_Outlier([160, 3, 1719, 19, 11, 13, -21]))

print(-21%2)
