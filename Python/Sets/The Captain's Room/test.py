from collections import Counter
k = int(input())
room_list = input().split()
count = Counter(room_list)
print(list(count.keys())[list(count.values()).index(1)])
