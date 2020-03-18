#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr, n):
    L = [0]*100
    for i in arr:
        L[i] += 1
    return L
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
