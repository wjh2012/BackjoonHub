def sol():
    N = int(input())

    if N==1:
        print(1)
        return
    elif N==2:
        print(1)
        return

    dp = [0]*N
    dp[0]=dp[1]=1
    for i in range(2,N):
        dp[i]=dp[i-2]+dp[i-1]
    print(dp[-1])
sol()