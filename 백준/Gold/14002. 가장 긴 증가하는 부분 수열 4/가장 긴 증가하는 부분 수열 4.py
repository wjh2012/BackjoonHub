import sys

def sol():
    N = int(sys.stdin.readline())
    A =  list(map(int,sys.stdin.readline().split()))
    dp = [0]*N

    for i in range(N):
        for j in range(i):
            if A[j] < A[i] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i]+=1

    result = []
    t=ans = max(dp)
    for i in range(N-1,-1,-1):
        if dp[i]==t:
            result.append(A[i])
            t-=1
    print(ans)
    print(*result[::-1])

sol()
