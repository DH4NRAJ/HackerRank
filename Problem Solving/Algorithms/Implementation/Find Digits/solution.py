#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def findDigits(n):
    L = [int(i) for i in str(n)]
    count = Counter(L)[0]
    for _ in range(count):
        L.remove(0)
    return sum([1 for i in L if n%i==0])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
