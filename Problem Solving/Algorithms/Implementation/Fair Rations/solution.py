#!/bin/python3

import math
import os
import random
import re
import sys

def fairRations(B):
    count=0
    for i in range(len(B)-1):
        if B[i]%2==1:
            B[i]+=1
            B[i+1]+=1
            count+=2
    if B[-1]%2==1:
        return 'NO'
    else:
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
