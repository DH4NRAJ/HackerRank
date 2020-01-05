N,X = map(int,input().split())
table = []
for _ in range(X):
    table.append( map(float, input().split()) )
for i in zip(*table): 
    print( sum(i)/len(i) )
