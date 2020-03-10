# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    i = n-1 
    v = arr[i]
    while (i>0 and v<arr[i-1]):
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = v
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
