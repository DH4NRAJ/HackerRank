from collections import Counter
N = int(input())
shop = Counter(list(map(int,input().split())))
n = int(input())
sum = 0
for _ in range(n):
    size,price = map(int,input().split())
    if (shop[size]>0):
        sum += price
        shop[size] -= 1
    else :
        pass
print(sum)
