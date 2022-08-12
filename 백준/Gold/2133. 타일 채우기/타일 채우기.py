import sys

def sol():
    N = int(sys.stdin.readline())      
    if N%2:
        print(0)
        return

    if N==2:
        print(3)
        return

    dp = [0]*(N//2)
    dp[0] = 3
    for i in range(1,N//2):
        dp[i] += dp[i-1]*3
        for j in range(2,i+1):
            dp[i] += dp[i-j]*2
        dp[i] += 2
        
    print(dp[N//2-1])

sol()