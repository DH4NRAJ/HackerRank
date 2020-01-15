#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            z += 1
        elif arr[i] > 0:
            p += 1
        else :
            n += 1
    t = len(arr)
    print("%.4f"%(p/t))
    print("%.4f"%(n/t))
    print("%.4f"%(z/t))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
