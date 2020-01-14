from collections import namedtuple
n = int(input())
student = namedtuple('student',input())
print(sum([int(student(*input().split()).MARKS)for _ in range(n)])/n)
