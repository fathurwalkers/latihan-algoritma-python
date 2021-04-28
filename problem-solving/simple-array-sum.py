import os
import sys
import math

arr = [2, 3, 6, 2, 1]

def doCount(arr):
    default = 0
    for i in range(len(arr)):
        default += arr[i]
    return(default)

print(doCount(arr))