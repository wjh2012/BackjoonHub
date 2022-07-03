import sys

def sol():
    n,m=map(int,input().split())
    a = sorted(list(map(int,sys.stdin.readline().split())))
    ans=[]

    def dfs():
        if len(ans)==m :
            print(*ans)
            return

        for i in range(n):
            if not ans or a[i]>=ans[-1]:
                ans.append(a[i])
                dfs()
                ans.pop()
    dfs()

sol()