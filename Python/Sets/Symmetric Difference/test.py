n = int(input())
A = set(map(int,input().split()))
m = int(input())
B = set(map(int,input().split()))
L = list(A^B)
L.sort()
print(*L,sep = "\n")
