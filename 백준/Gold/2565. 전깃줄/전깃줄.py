import sys

def sol():
    N = int(sys.stdin.readline())
    pole = []
    for _ in range(N):
        a,b = map(int,sys.stdin.readline().split())
        pole.append((a,b))
    
    pole.sort(key=lambda x:x[0])

    dp = [0]*(N)

    for i in range(N):
        for j in range(i):
            if pole[i][1] > pole[j][1] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i]+=1

    print(N-max(dp))

sol()