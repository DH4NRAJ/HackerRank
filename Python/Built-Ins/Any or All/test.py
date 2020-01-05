a,b = input(),input().split()
print(all(i[0] != '-'for i in b) and any(i == i[::-1]for i in b))
