import sys

def sol():
    n,m = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))

    mincut=0
    maxcut=max(a)
    while mincut<=maxcut:
        cut = (mincut+maxcut)//2

        have = 0
        for tree in a:
            if tree>cut:
                have+=(tree-cut)

        if have<m:
            maxcut=cut-1
        elif have>=m:
            mincut=cut+1

    print(maxcut)
    
sol()