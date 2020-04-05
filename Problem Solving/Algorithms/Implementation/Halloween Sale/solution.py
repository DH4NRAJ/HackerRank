#!/bin/python3
def split(n):
    if n <= 9:
        return n
    else:
         s = str(n)
         l = int(len(s)/2)
         a,b = s[:l],s[l:]
         return (int(a)+int(b))
def kaprekarNumbers(p, q):
    li = []
    for i in range(p,q+1):
        if( i== (split(i**2) )):
            li.append(i)
    if not li:
        print("INVALID RANGE")
    else:
        print(*li)



if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
