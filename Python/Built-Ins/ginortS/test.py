s = input()
u = list()
l = list()
d = list()
for i in range(len(s)):
    if s[i].isupper():
        u.append(s[i])
    elif s[i].islower():
        l.append(s[i])
    elif s[i].isdigit() :
        d.append(int(s[i]))
u.sort(),l.sort()
count = 0 
odd = []
even = []
for i in range(len(d)):
    if d[i]%2 != 0:
        odd.append(str(d[i]))
    else :
        even.append(str(d[i]))
odd.sort(),even.sort()
d = odd+even
print(''.join(l+u+d))
