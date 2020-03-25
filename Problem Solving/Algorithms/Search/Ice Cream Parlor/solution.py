#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr, n):
    ans = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j] == m:
                ans = [i+1, j+1]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr,n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
