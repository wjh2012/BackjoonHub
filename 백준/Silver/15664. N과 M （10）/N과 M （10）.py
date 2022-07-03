import sys

def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    ans=[]
    visited=[True]*n

    def dfs(idx):
        if len(ans)==m:
            print(*ans)
            return

        t=None
        for i in range(idx,n):
            if visited[i] and (not ans or a[i]>=ans[-1]):
                if a[i]!=t:
                    t=a[i]
                    visited[i]=False
                    ans.append(a[i])
                    dfs(idx+1)
                    ans.pop()
                    visited[i]=True
    dfs(0)

sol()