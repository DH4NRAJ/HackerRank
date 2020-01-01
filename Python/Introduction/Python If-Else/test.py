#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
assert(n<=100 and n>=1)
if (n%2 == 0):
    if (n>2 and n<5):
        print('Not Weird')
    elif (n>=6 and n<=20):
        print('Weird')
    else :
        print('Not Weird')
else :
    print('Weird')
    
    
    
    
    
'''
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])
#alternative     
'''
