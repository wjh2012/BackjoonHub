import sys

def heapify(arr, n, i):
    big = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[big] < arr[left]:
        big = left
    if right<n and arr[big] < arr[right]:
        big = right
    if big != i:
        arr[i], arr[big] = arr[big], arr[i]
        heapify(arr, n, big)

def heapinsert(arr,val):
    arr.append(val)
    i = len(arr)-1

    parent = (i-1)//2

    while arr[parent]<arr[i] and i!=0:
        arr[parent],arr[i] = arr[i],arr[parent]
        i=parent
        parent=(i-1)//2

    heapify(arr,len(arr),0)

def heapop(arr):
    print(arr[0])
    arr[0], arr[-1]=arr[-1], arr[0]
    del arr[-1]

    if arr:
        heapify(arr,len(arr),0)

def sol():
    N = int(sys.stdin.readline())
    heap = []
    for _ in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            if heap:
                heapop(heap)
            else:
                print(0)
        else:
            heapinsert(heap,x)

sol()