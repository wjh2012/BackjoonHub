import sys

def sol():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        p=[0,1,1,1]
        if N<4:
            print(p[N])
            continue
        if N>3:
            p.extend([0]*(N-3))
            for i in range(4,N+1):
                p[i]=p[i-3]+p[i-2]
            print(p[N])
sol()