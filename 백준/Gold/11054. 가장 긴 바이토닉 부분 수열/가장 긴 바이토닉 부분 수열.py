import sys

def sol():
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    B = A[::-1]

    dp = [0]*N
    pd = [0]*N

    ans = 0

    for i in range(N):
        for j in range(i):
            if A[i]>A[j] and dp[i]<dp[j]:
                dp[i] = dp[j]
            if B[i]>B[j] and pd[i]<pd[j]:
                pd[i] = pd[j]
        dp[i]+=1
        pd[i]+=1

    a = [x+y for x,y in zip(dp,pd[::-1])]
    print(max(a)-1)

sol()