import sys
sys.setrecursionlimit(10**9)
def sol():
    M, N = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    
    dp = [[-1]*N for _ in range(M)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def dfs(x,y):
        if x==M-1 and y==N-1:
            return 1

        if dp[x][y]!=-1:
            return dp[x][y]

        route = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>M-1 or ny>N-1:
                continue 
            if grid[nx][ny] < grid[x][y]:
                route += dfs(nx,ny)
        
        dp[x][y] = route
        return route

    dfs(0,0)

    print(dp[0][0])

sol()