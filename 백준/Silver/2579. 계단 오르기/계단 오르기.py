import sys

def sol():
    n=int(sys.stdin.readline())
    a=[]
    for _ in range(n):
        a.append(int(sys.stdin.readline()))
    
    
    b=[0]*n
    b[0]=a[0]
    if n>1:
        b[1]=a[0]+a[1] 
        for i in range(2,n):
            b[i] = max(b[i-3]+a[i-1]+a[i], b[i-2]+a[i])  
        
    
    print(b[n-1])

sol()