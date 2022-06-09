import sys

def sol():
    n=int(sys.stdin.readline())
    if n==1:
        print(n)
        return
        
    fib=[0]*(n+1)
    fib[1]=1
    fib[2]=2

    for i in range(3,n+1):
        fib[i]=fib[i-2]+fib[i-1]

    print(fib[n]%10007)
    
sol()