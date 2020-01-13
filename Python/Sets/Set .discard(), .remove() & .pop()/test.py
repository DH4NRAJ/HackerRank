
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    c = input().split()
    if c[0]=='pop':
        a = s.pop()
    elif c[0]=='remove':
        s.remove(int(c[1]))
    elif c[0]=='discard':
        s.discard(int(c[1]))
    else :
        pass
print(sum(s))
