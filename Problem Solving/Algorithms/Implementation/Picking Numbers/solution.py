#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    uniques = sorted(set(a))

    longest = int(0)

    for u in uniques:
        cur_length = len([x for x in a if x == u or x == u + 1])
        if cur_length > longest:
            longest = cur_length
    
    return longest
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
