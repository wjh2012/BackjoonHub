import sys

def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    ans=[]
    visited=[True]*n

    def dfs(idx):
        if len(ans)==m :
            print(*ans)
            return

        for i in range(idx,n):
            if visited[i]:
                visited[i]=False
                ans.append(a[i])
                dfs(i+1)
                ans.pop()
                visited[i]=True
    dfs(0)

sol()