import sys
    
def sol():
    N = int(sys.stdin.readline())
    home = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]

    # 1행 처리
    for i in range(1,N):
        if home[0][i]==1:
            break
        dp[0][i][0]=1

    # [행][열][0가로/1세로/2대각]
    for i in range(1,N):
        for j in range(2,N):
            if home[i][j]==1:
                continue
            # 가로->가로 / 대각->가로
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            # 세로->세로 / 대각->세로
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

            # 대각->대각 / 가로->대각 / 세로->대각
            if home[i-1][j]!=1 and home[i][j-1]!=1:
                dp[i][j][2] = dp[i-1][j-1][2] + dp[i-1][j-1][0] + dp[i-1][j-1][1]
    
    print(sum(dp[N-1][N-1]))

sol()