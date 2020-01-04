from itertools import combinations_with_replacement
str,n = input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(str),int(n))],sep='\n')
