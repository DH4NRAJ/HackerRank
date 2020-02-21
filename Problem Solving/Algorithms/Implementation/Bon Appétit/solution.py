nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
res = (sum(bill) - bill[k])/2
if res == b:
    print('Bon Appetit')
else :
    print(abs(int(res-b)))
