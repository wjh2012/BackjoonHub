import sys

def sol():
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        f = [0]+list(map(int,sys.stdin.readline().split()))
        dp = [[0]*(K+1) for _ in range(K+1)]

        accum = [0]*(K+1)
        for i in range(1,K+1):
            accum[i] = accum[i-1] + f[i]

        for size in range(2,K+1):
            for start in range(1,K-size+2):
                end = start+size-1

                val = 9999999999999
                for mid in range(start, end):
                    val = min(val, dp[start][mid]+dp[mid+1][end] + accum[end] - accum[start-1])
                dp[start][end] = val
                
        print(dp[1][-1])


sol()
