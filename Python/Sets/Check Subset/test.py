n = int(input())
for _ in range(n):
    a = int(input())
    A = set(map(int,input().split()))
    b = int(input())
    B = set(map(int,input().split()))
    print(A.issubset(B))
