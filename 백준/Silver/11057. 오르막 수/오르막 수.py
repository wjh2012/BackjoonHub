import sys

def sol():
    N = int(sys.stdin.readline())
    if N==1:
        print(10)
        return

    dp = [[0]*10 for _ in range(N+1)]
    dp[1] = [1]*10
    
    for i in range(2, N+1):
        for j in range(10):
            for t in range(j,10):
                dp[i][j] += dp[i-1][t]
    print(sum(dp[-1])%10007)


sol()