nd = input().split()

n = int(nd[0])

d = int(nd[1])

c = list(map(int, input().rstrip().split()))
gc = 0
for i in range(n):
    if c[i]+d in c and c[i]+2*d in c:
        gc+=1
print (gc)
