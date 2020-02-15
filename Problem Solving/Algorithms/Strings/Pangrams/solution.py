#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for c in alpha:
        if c not in s.lower():
            return 'not pangram'
            exit()
        else :
            pass
    return 'pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
