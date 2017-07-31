import math


def beggars(values,n):
    if n==0:
        return []
    takeHome=[0]*n
    for i in range(len(values)):

        takeHome[i%n]+=values[i]
    return takeHome


print(beggars([1,2,3,4,5],1))
