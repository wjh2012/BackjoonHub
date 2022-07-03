import sys
def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    ans = []
    
    def dfs(idx):
        if idx==m:
            print(*ans)
            return

        for i in range(n):
            if not ans or a[i]>=ans[-1]:
                ans.append(a[i])
                dfs(idx+1)
                ans.pop()
        
    dfs(0)

sol()
