#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(n, arr):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
