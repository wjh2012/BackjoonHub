from re import A
import sys

def sol():
    n=int(sys.stdin.readline())
    a = [0]*(n+1)
    
    for i in range(1,n+1):
        if (i**(1/2)).is_integer():
            a[i]=1
        else:
            root = int(i**(1/2))
            tmp=4
            for j in range(root, 0, -1):
                if a[i-(j**2)]<tmp:
                    tmp=a[i-(j**2)]+1
            a[i]=tmp

    print(a[n])
    
sol()