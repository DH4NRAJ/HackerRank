'''
#Noraml Way N>10
a = int(input())
for i in range(1,a+1):
    st = ""
    for x in range(1,i+1):
        st += str(x)
    y = i-1
    while (y>0):
        st += str(y)
        y-=1
    print(st)
'''
for i in range(0,int(input())):
    print ([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321, 12345678910987654321][i])
