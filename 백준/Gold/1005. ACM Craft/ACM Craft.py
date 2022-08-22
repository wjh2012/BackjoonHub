import sys
from collections import deque

def sol():
    T = int(sys.stdin.readline())
    for _ in range(T):
        # 건물 개수 / 순서 개수
        N, K = map(int, sys.stdin.readline().split())
        # 건설 시간
        D = list(map(int, sys.stdin.readline().split()))
        
        indegree = [0]*(N+1)
        graph = [[] for _ in range(N+1)]
        
        # 건설 순서
        for _ in range(K):
            X,Y = map(int, sys.stdin.readline().split())
            graph[X].append(Y)
            indegree[Y] += 1

        # 목표 건물
        W = int(sys.stdin.readline())

        dq = deque()
        dp = [0]*(N+1)

        # 진입노드가 없는 노드
        for i in range(1, N+1):
            if indegree[i] == 0:
                dq.append(i)
                dp[i] += D[i-1]

        
        while dq:
            x = dq.popleft()
            
            for i in graph[x]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[x] + D[i-1])

                if indegree[i] == 0:
                    dq.append(i)

        print(dp[W])

sol()
