import math,os, sys,random,time,turtle,operator
import datetime

def how_to_find_them(right_triangle):
    a,b,c=0,0,0
    try:
        a=right_triangle["a"]
    except:
        None
    try:
        b=right_triangle["b"]
    except:
        None
    try:
        c=right_triangle["c"]
    except:
        None

    if a==0:
        missing="a"
    elif b==0:
        missing="b"
    elif c==0:
        missing="c"

    other=a**2+b**2
    right=c**2
    d=0

    if other>right:
        c=a
        while other>=right:
            c+=0.001
            right=c**2
            right_triangle[missing]=round(c,3)

    elif other<right:
        temp=right-other
        dSq=d**2
        while temp>=dSq:
            d+=0.001
            dSq=d**2
        right_triangle[missing]=round(d,3)

    return right_triangle



right_triangle={"b":2,"c":3}

print(how_to_find_them(right_triangle))
