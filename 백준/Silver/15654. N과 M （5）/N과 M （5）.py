import sys
def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    ans = []
    visited = [False]*n
    
    def dfs(idx):
        if idx==m:
            print(*ans)
            return

        for i in range(n):
            if not visited[i]:
                visited[i]=True
                ans.append(a[i])
                dfs(idx+1)
                ans.pop()
                visited[i]=False
        
    dfs(0)

sol()