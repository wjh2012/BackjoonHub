import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    
    q=1
    for x in range(1,m+1):
        q*=x
    w=1    
    for y in range(1,m-n+1):
        w*=y
    e=1
    for z in range(1,n+1):
        e*=z
    print(q//w//e)