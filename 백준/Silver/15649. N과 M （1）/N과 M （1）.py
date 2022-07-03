def sol():
    n,m=map(int,input().split())
    visited = [True]*n
    ans=[]

    def dfs():
        if len(ans)==m :
            print(*ans)
            return

        for i in range(n):
            if visited[i]:
                visited[i]=False
                ans.append(i+1)
                dfs()
                ans.pop()
                visited[i]=True

    dfs()

sol()