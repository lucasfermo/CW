import math


def find_deleted_number(arr,mixed_arr):
    missing=False
    for i in arr:
        if i not in mixed_arr:
            missing=True
            num=i
    if missing:
        return num
    else:
        return 0

print(find_deleted_number([1,2,3,4,5,6,7,8,9], [7,6,9,4,8,1,2,3]))
