lst=[0]
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    if(a[0]==1):
        lst.append(a[1] if a[1]>lst[-1] else lst[-1])
    elif(a[0]==2):
        lst.pop()
    elif(a[0]==3):
        print(lst[-1])
        
        

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def printmax(self):
        return max(self.items)

s = Stack()
tests = int(input())
for i in range(tests):
    ii  = input()
    if len(ii)>1:
        num, item = map(int, ii.split())
        s.push(item)
    else:
        if ii == '2':
            _ = s.pop()
        else :
            print(s.printmax())

"""
