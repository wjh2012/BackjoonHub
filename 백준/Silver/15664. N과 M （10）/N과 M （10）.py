import sys

def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    ans=[]

    def dfs(idx):
        if len(ans)==m:
            print(*ans)
            return

        t=None
        for i in range(idx,n):
            if not ans or a[i]>=ans[-1]:
                if a[i]!=t:
                    t=a[i]
                    ans.append(a[i])
                    dfs(i+1)
                    ans.pop()
    dfs(0)

sol()