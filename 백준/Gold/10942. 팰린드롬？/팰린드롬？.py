import sys
sys.setrecursionlimit(10**6)
def sol():
    N = int(sys.stdin.readline())
    A =  [0]+list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [[-1]*(N+1) for _ in range(N+1)]

    def fel(s,e):
        if s == e:
            return 1
        elif s+1 == e:
            if A[s] == A[e]:
                return 1
            else:
                return 0

        if A[s] == A[e]:
            # 방문한 적이 없으면
            if dp[s+1][e-1] == -1:
                dp[s][e] = fel(s+1,e-1)
                return dp[s][e]
            # 방문 했었으면
            else:
                dp[s][e] = dp[s+1][e-1]
                return dp[s][e]
        else:
            dp[s][e] = 0
            return 0
    
    for _ in range(M):
        S,E = map(int,sys.stdin.readline().split())
        if S==E:
            print(1)
        else:
            print(fel(S,E))


sol()
