i, j, k = [int(x) for x in input().split()]
Day = [1 for d in range(i, j+1) if (d-(int(str(d)[::-1])))%k == 0]
print(sum(Day))
