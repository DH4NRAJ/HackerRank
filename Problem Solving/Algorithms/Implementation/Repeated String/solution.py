s, n = input().strip(), int(input().strip())
ls = len(s)
print((s.count('a') * (n//ls + 1))-(s[n%ls:].count('a')))
