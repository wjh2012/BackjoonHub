import sys
from collections import defaultdict

def sol():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n==0:
            print(0)
            continue

        cloth = defaultdict(list)
        for _ in range(n):
            name, categ = sys.stdin.readline().split()
            cloth[categ].append(name)
        
        x=[len(x) for x in cloth.values()]
        ans=1
        for i in x:
            ans*=(i+1)
        print(ans-1)
sol()