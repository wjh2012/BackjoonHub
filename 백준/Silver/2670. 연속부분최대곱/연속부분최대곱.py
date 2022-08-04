import sys

def sol():
    N = int(sys.stdin.readline())
    f = [float(sys.stdin.readline()) for _ in range(N)]
    dp = [0]*N
    dp[0] = f[0]

    if N == 1:
        print(f[0])
        return
        
    for i in range(1,N):
        dp[i] = max(dp[i-1]*f[i], f[i])

    print(f'{max(dp):0.3f}')

sol()