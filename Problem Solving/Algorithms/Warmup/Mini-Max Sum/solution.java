#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    miN =  min(arr)
    maX =  max(arr)
    print((sum(arr)-maX),(sum(arr)-miN))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
