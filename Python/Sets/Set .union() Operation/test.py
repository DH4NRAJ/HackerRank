n = int(input())
eng = set(map(int,input().split()))
m = int(input())
frn = set(map(int,input().split()))
print(len(eng|frn))

