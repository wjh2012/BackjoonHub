import sys
from collections import deque

def spread(OriMap):
    global N, M, virus

    Map = [[0]*(M+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(M+2):
            Map[i][j]=OriMap[i][j]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for p,q in virus:
        dq = deque([(p,q)])

        while dq:
            x,y = dq.popleft()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]

                if Map[nx][ny]==0:
                    Map[nx][ny]=2
                    dq.append((nx,ny))

    c=0
    for i in range(N+2):
        for j in range(M+2):
            if Map[i][j]==0:
                c+=1
    return c
    
def dfs(Map,n):
    global N,M,virus,ans

    if n==3:
        ans.append(spread(Map))
        return
    
    for i in range(1,N+1):
        for j in range(1,M+1):
            if Map[i][j]==0:
                Map[i][j]=1
                dfs(Map,n+1)
                Map[i][j]=0


def sol():
    global N,M,virus,ans
    N,M = map(int,input().split())
    
    ans = []
    Map = []
    virus = []

    Map.append([1]*(M+2))
    for _ in range(N):
        Map.append([1]+list(map(int,sys.stdin.readline().split()))+[1])
    Map.append([1]*(M+2))

    for i in range(1,N+1):
        for j in range(1,M+1):
            if Map[i][j]==2:
                virus.append((i,j))

    dfs(Map,0)
    print(max(ans))

sol()