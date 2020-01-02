if __name__ == '__main__':
    n = int(input())
    list = list(map(int, input().split()))
    z = max(list)
    while max(list)==z:
        list.remove(max(list))
    print(max(list))
