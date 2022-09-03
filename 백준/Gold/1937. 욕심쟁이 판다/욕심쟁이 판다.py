import sys
sys.setrecursionlimit(10**9)
def sol():
    n = int(sys.stdin.readline())
    bamboo = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    
    dp = [[-1]*n for _ in range(n)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def dfs(x,y):
        if dp[x][y] == -1:
            dp[x][y] = 0

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                # 지금 위치보다 대나무가 많고,
                # 이미 방문했던 지역이라면
                if n>nx>=0 and n>ny>=0 and bamboo[nx][ny] > bamboo[x][y]:
                    dp[x][y] = max(dp[x][y], dfs(nx,ny))
        
        return dp[x][y] + 1
    
    ans=0
    for i in range(n):
        for j in range(n):
            ans = max(ans, dfs(i,j))

    print(ans)

sol()
