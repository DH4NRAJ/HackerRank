import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = input().split()
    print(" ".join(arr[m:]+arr[:m]))
