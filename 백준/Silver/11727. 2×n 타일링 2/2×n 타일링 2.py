import sys

def sol():
    n = int(sys.stdin.readline())
    if n==1:
        print(1)
        return

    a=[0,1]+[0]*(n-1)
    for i in range(2,n+1):
        if i%2==0:
            a[i]=a[i-1]*2+1
        else:
            a[i]=a[i-1]*2-1
    print(a[n]%10007)
sol()