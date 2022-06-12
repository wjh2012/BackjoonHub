import sys
from collections import deque

def sol():
    N,M = map(int,sys.stdin.readline().split())
    grid=[]
    for _ in range(N):
        grid.append(list(map(int,sys.stdin.readline().rstrip())))

    dq=deque()
    dq.append((0,0))
    
    while dq:
        x,y=dq.popleft()
        if (x,y)==(N-1,M-1):
            print(grid[x][y])
            break

        if x-1>=0 and grid[x-1][y]==1:
            dq.append((x-1,y))
            grid[x-1][y]=grid[x][y]+1

        if x+1<N and grid[x+1][y]==1:
            dq.append((x+1,y))
            grid[x+1][y]=grid[x][y]+1

        if y-1>=0 and grid[x][y-1]==1:
            dq.append((x,y-1))
            grid[x][y-1]=grid[x][y]+1

        if y+1<M and grid[x][y+1]==1:
            dq.append((x,y+1))
            grid[x][y+1]=grid[x][y]+1


sol()