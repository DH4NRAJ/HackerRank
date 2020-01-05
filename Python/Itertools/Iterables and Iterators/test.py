from itertools import combinations
n , l  = (input().split() for _ in range(2))
k = int(input())
comb = list(combinations(l,k))
filtered_comb = [x for x in comb if 'a' in x]
print(len(filtered_comb)/len(comb))
