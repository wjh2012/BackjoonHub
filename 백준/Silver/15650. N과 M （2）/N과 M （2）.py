def sol():
    n,m=map(int,input().split())
    visited = []
    
    def dfs(v, idx):
        if len(v)==m:
            print(*v)
            return

        for i in range(idx,n+1):
            if i not in visited:
                visited.append(i)
                dfs(v,i+1)
                visited.pop()

    dfs(visited, 1)

sol()