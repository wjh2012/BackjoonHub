import sys
from collections import deque

ans = 0

def sol():
    N,M = map(int,input().split())
    Map = []
    virus = []

    def spread():
        TestMap = [[1]*(M+2)for _ in range(N+2)]
        for i in range(1,N+1):
            for j in range(1,M+1):
                TestMap[i][j] = Map[i][j]

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for p,q in virus:
            dq = deque([(p,q)])
            while dq:
                x,y = dq.popleft()
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if TestMap[nx][ny]==0:
                        TestMap[nx][ny]=2
                        dq.append((nx,ny))
        c = 0
        for i in range(1,N+1):
            for j in range(1,M+1):
                if TestMap[i][j]==0:
                    c+=1
        return c

    def dfs(n):
        global ans
        if n==3:
            ans = max(ans,spread())
            return
        for i in range(1,N+1):
            for j in range(1,M+1):
                if Map[i][j]==0:
                    Map[i][j]=1
                    dfs(n+1)
                    Map[i][j]=0

    # 기본 지도 생성
    Map.append([1]*(M+2))
    for _ in range(N):
        Map.append([1]+list(map(int,sys.stdin.readline().split()))+[1])
    Map.append([1]*(M+2))
    # 시작 바이러스 위치
    for n in range(1,N+1):
        for m in range(1,M+1):
            if Map[n][m]==2:
                virus.append((n,m))
    
    dfs(0)

sol()
print(ans)