N = int(input())
L =[]
for _ in range(N):
    L.append(input())
n = int(input())
l = []
for _ in range(n):
    l.append(input())
for i in range(n):
    count = 0
    for j in range(N):
        if (l[i] == L[j]):
            count += 1
        else :
            pass
    print(count)
