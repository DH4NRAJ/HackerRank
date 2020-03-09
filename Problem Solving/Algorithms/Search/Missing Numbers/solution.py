#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    s=[]
    for x in range(max(brr)+1):
        s.append(0)
    for x in range(len(brr)):
        s[brr[x]]=s[brr[x]]+1
    for y in range(len(arr)):
        s[arr[y]]=s[arr[y]]-1       
    li=[]
    for x in range(len(s)):
        if(s[x]==0):
            continue
        else:
            li.append(x)
    li.sort()
    return li
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
