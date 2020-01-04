import math
a = int(input())
b = int(input())
print (divmod(a,b)[0],divmod(a,b)[1],divmod(a,b),sep="\n")

'''
#Effective Way
print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))
'''
