import math,os, sys,random,time,turtle,operator
import datetime

def sqInRect(lng,width):
    if lng==width:
        return None
    rectangles=[]
    total=lng*width
    while width!=lng:
        size=min(lng,width)
        rectangles.append(size)
        if lng>width:
            lng-=size
        else:
            width-=size
    rectangles.append(lng)
    return rectangles



print(sqInRect(5,3))
