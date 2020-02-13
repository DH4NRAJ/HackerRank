#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    Mi = Ma = scores[0]
    Mi_count = Ma_count = 0
    for i in range(len(scores)):
        if scores[i] > Ma:
            Ma_count += 1
            Ma = scores[i]
        elif scores[i] < Mi:
            Mi_count += 1
            Mi = scores[i]
    return [Ma_count, Mi_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
