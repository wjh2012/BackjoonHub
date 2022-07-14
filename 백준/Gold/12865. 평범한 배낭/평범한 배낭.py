import sys
    
def sol():
    N, limit = map(int,sys.stdin.readline().split())
    wList = []
    vList = []
    for _ in range(N):
        w,v = map(int,sys.stdin.readline().split())
        wList.append(w)
        vList.append(v)
    
    dp = [[0]*(limit+1) for _ in range(N+1)]
    
    for i in range(N+1):

        for w in range(limit+1):

            if i==0 or w==0:
                dp[i][w]=0
                continue

            if wList[i-1] <= w:
                dp[i][w] = max(vList[i-1]+dp[i-1][w-wList[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print(dp[N][limit])

sol()