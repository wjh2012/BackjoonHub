import sys
    
def sol():
    N,M = map(int,sys.stdin.readline().split())
    grid = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    
    for i in range(N):
        dp[i][0]=grid[i][0]
        for j in range(1,N):
            dp[i][j]+=dp[i][j-1]+grid[i][j]
            
    for _ in range(M):
        x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

        x1-=1
        y1-=1
        x2-=1
        y2-=1
        
        ans = 0

        if y1==0:
            for i in range(x1,x2+1):
                ans += dp[i][y2]
            print(ans)
            continue

        for i in range(x1,x2+1):
            ans += dp[i][y2]-dp[i][y1-1]

        print(ans)

sol()