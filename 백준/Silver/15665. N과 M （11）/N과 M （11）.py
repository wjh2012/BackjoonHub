import sys

def sol():
    _,m=map(int,input().split())
    a = sorted(list(set(map(int,sys.stdin.readline().split()))))
    ans=[]
    n=len(a)
    
    def dfs():
        if len(ans)==m:
            print(*ans)
            return

        for i in range(n):
            ans.append(a[i])
            dfs()
            ans.pop()
    dfs()

sol()