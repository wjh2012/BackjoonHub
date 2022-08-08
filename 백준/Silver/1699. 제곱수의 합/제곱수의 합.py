import sys

def sol():
    N = int(sys.stdin.readline())

    dp = [0]*(N+1)
    dp[1]=1

    for i in range(2,N+1):
        dp[i]=i
        t = int(i**(1/2))
        for j in range(t+1):
            dp[i] = min(dp[i], dp[i-j*j] + 1)
    print(dp[-1])

sol()