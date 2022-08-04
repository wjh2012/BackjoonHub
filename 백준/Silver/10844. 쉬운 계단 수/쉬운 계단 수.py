import sys

def sol():
    N = int(sys.stdin.readline())
    if N==1:
        print(9)
        return

    dp = [[0]*11 for _ in range(N+1)]
    dp[1] = [0]+[1]*9+[0]
    dp[2] = [0]+[2]*8+[1]+[0]
    for i in range(3,N+1):
        for j in range(1,10):
            if j == 1:
                dp[i][j] = dp[i-2][j] + dp[i-1][j+1]
                continue
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    
    print(sum(dp[-1])%1000000000)

sol()
