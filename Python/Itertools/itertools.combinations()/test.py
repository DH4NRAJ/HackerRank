from itertools import combinations
str,n = input().split()
a = 1
while a<=int(n): 
    print(*[''.join(i) for i in combinations(sorted(str),int(a))],sep='\n')
    a+=1
