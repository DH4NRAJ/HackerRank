import re
for _ in range(int(input())):
    flag = True
    try:
        reg = re.compile(input())
    except re.error:
        flag = False
    print(flag)
