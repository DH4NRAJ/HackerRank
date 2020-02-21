#!/bin/python3
import os
def appendAndDelete(s, t, k):
    a = len(s)
    b = len(t)
    c = 0
    for i in range(0, min(a,b),1):
        if(s[i] == t[i]):
            c+=1
        else:
            break
    if(a+b-2*c > k):
        return 'No'
    elif((a+b-2*c)%2 == k%2):
        return 'Yes'
    elif(a+b-k < 0):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
