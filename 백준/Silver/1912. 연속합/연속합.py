import sys

def sol():
    n = int(input())
    num = [0]+list(map(int,sys.stdin.readline().split()))

    dp = [0]*(n+1)
    dp[0] = -1000

    ans = -1000
    for i in range(1,n+1):
        if dp[i-1] < 0 and num[i] < 0:
            dp[i] = max(num[i], dp[i-1])
        else:
            k = dp[i-1] + num[i]
            dp[i] = max(k, num[i])

        ans = max(ans, dp[i])

    print(ans)

sol()