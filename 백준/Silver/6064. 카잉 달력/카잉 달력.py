import sys

def sol():
    T = int(input())
    for _ in range(T):
        M,N,x,y = map(int, sys.stdin.readline().split())
        
        while x<=M*N:
            if (x-y)%N==0:
                print(x)
                break
            x+=M
        if x>M*N:
            print(-1)
        
sol()