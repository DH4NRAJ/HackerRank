#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_oranges = count_apple = 0 
    for i in apples:
        if a+i in range(s, t+1):
            count_apple += 1
    for i in oranges:
        if b+i in range(s, t+1):
            count_oranges += 1
    print(count_apple, count_oranges , sep = '\n') 

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
