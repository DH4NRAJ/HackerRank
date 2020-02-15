#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    L = []
    for i in s:
        if not L:
            L.append(i)
        else:
            if L[-1] == i:
                L.pop()
            else :
                L.append(i)
    return ('Empty String' if not L else ''.join(L))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
