from collections import defaultdict
n,m = map(int,input().split())
a = defaultdict(list)
for i in range(1,n+1):
    a[input()].append(i)
for i in range(m):
    c = input()
    if (c not in a.keys()):
        print(-1)
    else:
        print(*a[c])
