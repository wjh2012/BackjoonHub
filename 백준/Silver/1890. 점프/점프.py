import sys

def sol():
    N = int(sys.stdin.readline())
    grid = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                print(dp[i][j])
                return
            move = grid[i][j]
            if i + move < N:
                dp[i + move][j] += dp[i][j]
            if j + move < N:
                dp[i][j + move] += dp[i][j]

sol()
