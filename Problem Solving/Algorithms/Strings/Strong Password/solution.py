#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    count = 0    
    if not any(i.isdigit() for i in password):
        count+=1
    if not any(i.islower() for i in password):
        count+=1
    if not any(i.isupper() for i in password):
        count+=1
    if not any(i in '!@#$%^&*()-+' for i in password):
        count+=1
    return max(count,6-n)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
