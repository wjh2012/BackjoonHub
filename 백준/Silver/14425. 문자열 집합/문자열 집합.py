import sys
from collections import defaultdict

def sol():
    n,m=map(int,sys.stdin.readline().split())
    
    s=set()
    c=defaultdict(int)

    for _ in range(n):
        s.add(sys.stdin.readline().rstrip())
    for _ in range(m):
        c[sys.stdin.readline().rstrip()]+=1
    cc = set(c.keys())

    sc = s & cc
    ans = 0
    
    for i in sc:
        ans+=c[i]
    print(ans)


sol()