import sys

def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    visited=[False]*n
    ans=[]

    def dfs():
        if len(ans)==m:
            print(*ans)
            return
        rem = 0
        for i in range(n):
            if not visited[i] and a[i]!=rem:
                visited[i]=True
                ans.append(a[i])
                rem=a[i]
                dfs()
                ans.pop()
                visited[i]=False

    dfs()

sol()