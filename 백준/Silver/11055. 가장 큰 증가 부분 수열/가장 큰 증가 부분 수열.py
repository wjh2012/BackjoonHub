import sys

def sol():
    N = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))    

    dp = [0]*N
    
    for i in range(N):
        for j in range(i):
            if a[i]>a[j] and dp[i]<dp[j]:
                dp[i]=dp[j]
        dp[i]+=a[i]

    print(max(dp))

sol()