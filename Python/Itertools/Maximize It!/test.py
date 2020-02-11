import itertools

lines,m = input().split()
final=[]
for i in range(0,int(lines)):
    input_list = [int(x)**2 for x in input().split()]
    final.append(input_list[1:])

res = list(itertools.product(*final))
Sum = [sum(x)%int(m) for x in res]
print(max(Sum))
