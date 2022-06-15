import sys

def sol():
    N,M = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))

    b=[a[0]]+[0]*(N-1)
    for i in range(N):
        b[i]=b[i-1]+a[i]

    for _ in range(M):
        i,j = map(int,sys.stdin.readline().split())
        if i==1:
            print(b[j-1])
            continue
        print(b[j-1]-b[i-2])
sol()