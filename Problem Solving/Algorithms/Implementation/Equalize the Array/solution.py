#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def equalizeArray(arr):
    occurence_count = Counter(arr) 
    element =  occurence_count.most_common(1)[0][0]
    return len(arr) - occurence_count[element]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
