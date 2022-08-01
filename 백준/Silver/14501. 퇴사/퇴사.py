import sys

def sol():
    N = int(input())
    T = [0]
    P = [0]

    for _ in range(N):
        t,p = map(int,sys.stdin.readline().split())
        T.append(t)
        P.append(p)

    dp = [0]*(N+2)
    
    for i in range(N, 0, -1):
        dDay = i + T[i]
        if dDay > N + 1:
            dp[i] = dp[i+1]
            continue
        dp[i] = max(P[i] + dp[dDay], dp[i+1])
    print(dp[1])

sol()