import math,os, sys,random,time,turtle,operator
import datetime


def is_interesting(number,awesome_phrases):
    if number==98 or number== 99:
         return 1
    if check(number,awesome_phrases):
        return 2
    elif check(number+1,awesome_phrases) or check(number+2,awesome_phrases):
        return 1
    return 0



def check(number,awesome_phrases):
    string=str(number)
    length=len(string)
    if length<3:
        return False
    same=True
    for i in string:
        if i!=string[0]:
            same=False
    if same:
        return True
    less=length-1
    if string[1:length]=="0"*less: #Check for zeroes
        return True
    inc="1234567890"
    dec="9876543210"
    if string in inc or string in dec:
        return True
    pal=True
    if string[:]==string[::-1]: #Check for palindrome
        return True
    for i in awesome_phrases:
        if string in str(i):
            return True
    return False

awesome=[1337,256]

print(is_interesting(1336,awesome))
