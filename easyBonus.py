import math

def bonus_time(salary,bonus):
    return "$"+str(salary*10) if bonus else "$"+str(salary)

print(bonus_time(5,False))
