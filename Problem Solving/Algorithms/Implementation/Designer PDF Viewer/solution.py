#!/bin/python3

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    L = list()
    for i in word.lower():
        L.append(h[ord(i)-97])
    return max(L)*len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
