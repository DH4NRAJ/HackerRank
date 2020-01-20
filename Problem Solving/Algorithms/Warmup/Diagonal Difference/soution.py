#!/bin/python3

import math
import os 
import sys

def diagonalDifference(arr):
    p = 0 
    s = 0
    l = len(arr[0])
    for i in range(l):
        p += arr[i][i]
        s += arr[i][l-i-1]
    return abs(p-s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
