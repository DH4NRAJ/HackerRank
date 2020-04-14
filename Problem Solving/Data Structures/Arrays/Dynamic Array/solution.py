#!/bin/python3

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastans = 0
    for q in queries:
        if q[0] == 1:
            arr[(q[1]^lastans)%n].append(q[2])
        else:
            idx  = (q[1]^lastans)%n
            lastans = arr[idx][q[2]%len(arr[idx])]
            print(lastans)

            
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
