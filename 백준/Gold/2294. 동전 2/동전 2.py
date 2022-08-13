import sys
INF = 99999999999999999
def sol():
    n,k = map(int,sys.stdin.readline().split())
    wallet = [int(sys.stdin.readline()) for _ in range(n)]
    
    dp = [INF] * (k+1)
    dp[0] = 0
    for coin in wallet:
        for j in range(coin, k+1):
            dp[j] = min(dp[j], dp[j-coin]+1)
    
    ans = dp[-1]
    if ans == INF:
        print(-1)
    else:
        print(dp[-1])

sol()