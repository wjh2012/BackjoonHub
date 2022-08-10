import sys

def sol():
    N, K = map(int,sys.stdin.readline().split())

    N-=1
    K-=1

    a = 1
    b = 1
    if N-K < K:
        for i in range(K+1,N+1):
            a*=i
        for i in range(1,N-K+1):
            b*=i
        print(a//b)
    else:
        for i in range(N-K+1,N+1):
            a*=i
        for i in range(1,K+1):
            b*=i
        print(a//b)

sol()