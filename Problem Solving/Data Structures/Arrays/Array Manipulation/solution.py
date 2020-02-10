#!/bin/python3

import os
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries, m):
    arr = [0]*n
    for i in range(0,m):
        a = queries[i][0] - 1
        b = queries[i][1]
        c = queries[i][2]
        for k in range(a, b):
            arr[k] += c
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries, m)

    fptr.write(str(result) + '\n')

    fptr.close()
