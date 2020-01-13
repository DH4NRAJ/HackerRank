n = int(input())
A = set(map(int,input().split()))
n = int(input())
for _ in range(n):
    l = input().split()
    if l[0] == 'intersection_update':
        A.intersection_update(set(map(int,input().split())))
    elif l[0] == 'update':
        A.update(set(map(int,input().split())))
    elif l[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(set(map(int,input().split())))
    elif l[0] == 'difference_update':
        A.difference_update(set(map(int,input().split())))
    else :
        pass
print(sum(A))
