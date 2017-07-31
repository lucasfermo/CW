import math,os, sys,random,time,turtle,operator
import datetime

#Sort climbing grades

def sortGrades(lst):
    if len(lst)==0:
        return []
    ranks={"Z":-1,"VB":0,"V0":1,"V0+":2}
    for i in range(3,20):
        ranks["V"+str(i-2)]=i
    lst=list(set(lst))
    final=[]
    for i in range(len(lst)):
        max=0
        for j in range(len(lst)):
            if ranks[lst[j]]>=max:
                max=ranks[lst[j]]
                index=j
        final.append(lst[index])
        lst[index]="Z"
    final=final[::-1]


    return final

print(sortGrades(['V13', 'V14', 'VB', 'V0']))
