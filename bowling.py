import math

def bowling_pins(arr):
    pins="6 7 8 9\n 3 4 5 \n  1 2  \n   0   "

    for i in arr:
        if str(i-1) in pins:
            pins=pins.replace(str(i-1)," ")
    pins=list(pins)
    for i in range(len(pins)):
        if pins[i].isdigit():
            pins[i]="I"

    pins="".join(pins)
    return pins


'I   I I\n I I I \n  I I  \n       '
'    I  \n I I I \n    I  \n       '



print(bowling_pins([8,1,10,2,7]))
