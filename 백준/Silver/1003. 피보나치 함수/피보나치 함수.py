import sys

def sol():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n>1:
            fib=[0]*(n+1)
            fib[0]=0
            fib[1]=1
            for i in range(2, n+1):
                fib[i]=fib[i-1]+fib[i-2]
            print(fib[n-1], fib[n])
        else:
            if n==0:
                print(1, 0)
            elif n==1:
                print(0, 1)
sol()