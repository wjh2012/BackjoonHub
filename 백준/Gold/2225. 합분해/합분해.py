import sys

def sol():
    N,K = map(int,sys.stdin.readline().split())
    
    dp = [[0] * (N+1) for _ in range(K+1)]
    
    for i in range(N+1):
        dp[1][i] = 1

    # 갯수
    for count in range(2,K+1):
        # 목표 숫자
        for num in range(N+1):
            for i in range(num+1):
                dp[count][num] += dp[count-1][num-i]
    
    print(dp[-1][-1]%1000000000)

sol()