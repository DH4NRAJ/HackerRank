#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    ans = [0]*100
    res = []
    for i in arr:
        ans[i]+=1
    
    for v in range(100):
        res+= [v]*ans[v]
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
