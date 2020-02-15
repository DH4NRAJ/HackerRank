def funnyString(s):
    L = [ord(c) for c in s]
    RL = L[::-1]
    resL = []
    resRL = []
    for i in range(1, len(L)):
        resL.append(abs(L[i-1]-L[i]))
        resRL.append(abs(RL[i-1]-RL[i]))
    return 'Funny' if resL == resRL else 'Not Funny'

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)
