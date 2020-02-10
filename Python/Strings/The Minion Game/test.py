def minion_game(string):
    vowels=['A','E','I','O','U']
    n=len(s)
    kev=0
    for i in range(n):
        if string[i] in vowels:
            kev+=n-i
    stu=(n*(n+1))//2 -kev
    if kev>stu:
        print('Kevin',kev)
    elif kev==stu:
        print('Draw')
    else:
        print('Stuart',stu)

if __name__ == '__main__':
    s = input()
    minion_game(s)
