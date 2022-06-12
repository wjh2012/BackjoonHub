import sys
from collections import deque

def sol():
    N,M = map(int,sys.stdin.readline().split())
    grid=[[0]*(M+2)]
    for _ in range(N):
        grid.append([0]+list(map(int,sys.stdin.readline().rstrip()))+[0])
    grid.append([0]*(M+2))

    dq=deque()
    dq.append((1,1))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while dq:
        x,y=dq.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if grid[nx][ny]==0:
                continue

            if grid[nx][ny]==1:
                dq.append((nx,ny))
                grid[nx][ny]=grid[x][y] + 1      

    print(grid[N][M])

sol()