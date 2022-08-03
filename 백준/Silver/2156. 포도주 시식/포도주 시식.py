import sys

def sol():
    n = int(input())
    wine = [int(sys.stdin.readline()) for _ in range(n)]
    
    if n==1:
        print(wine[0])
        return

    dp = [0]*n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]

    if n==2:
        print(dp[1])
        return

    dp[2] = max(wine[0] + wine[2], wine[0] + wine[1], wine[1]+wine[2])

    if n==3:
        print(dp[2])
        return

    for i in range(3,n):
        dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
        dp[i] = max(dp[i], dp[i-1])
    print(dp[-1])

sol()
