def birthdayCakeCandles(ar):
    count = 0 
    a = max(ar)
    for i in range(len(ar)):
        if ar[i] == a:
            count += 1
        else:
            pass
    print(count)
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
