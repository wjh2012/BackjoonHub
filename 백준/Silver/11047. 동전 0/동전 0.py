import sys

def sol():
    n, k= map(int,sys.stdin.readline().split())
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline()))

    count=0
    while k>0:
        for i in range(n-1,-1,-1):
            x = k//a[i]
            if x>0:
                k-=x*a[i]
                count+=x
                break
    print(count)

sol()

