import sys

def sol():
    n, k = map(int,sys.stdin.readline().split())
    wallet = [int(sys.stdin.readline()) for _ in range(n)]

    dp = [0]*(k+1)
    # 0원을 만드는 경우는 1가지(모두 선택 X)
    dp[0] = 1

    for coin in wallet:
        for target in range(coin, k+1):
            dp[target] += dp[target-coin]

    print(dp[-1])

sol()