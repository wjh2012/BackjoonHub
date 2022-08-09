import sys
import decimal
def sol():
    N, K = map(int,sys.stdin.readline().split())

    if K == 0 or N==K:
        print(1)
        return

    dp = [1]*(N+1)

    if N-K < K:
        for i in range(K+1,N+1):
            dp[i] = dp[i-1]*i
        for i in range(1,N-K+1):
            dp[i] = dp[i-1]*i
        print(dp[N]//dp[N-K]%10007)

    else:
        for i in range(N-K+1,N+1):
            dp[i] = dp[i-1]*i
        for i in range(1,K+1):
            dp[i] = dp[i-1]*i
        print(dp[N]//dp[K]%10007)

sol()