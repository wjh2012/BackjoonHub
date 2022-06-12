import sys
from collections import deque

def sol():
    N,M = map(int,sys.stdin.readline().split())
    grid=[]
    for _ in range(N):
        grid.append(list(map(int,sys.stdin.readline().rstrip())))

    dq=deque()
    dq.append((0,0))
    visited=[]
    
    while dq:
        x,y=dq.popleft()
        visited.append((x,y))
        if (x,y)==(N-1,M-1):
            print(grid[x][y])
            break

        if x-1>=0 and grid[x-1][y]!=0 and (x-1,y) not in visited and (x-1,y) not in dq:
            dq.append((x-1,y))
            grid[x-1][y]=grid[x][y]+1

        if x+1<N and grid[x+1][y]!=0 and (x+1,y) not in visited and (x+1,y) not in dq:
            dq.append((x+1,y))
            grid[x+1][y]=grid[x][y]+1

        if y-1>=0 and grid[x][y-1]!=0  and (x,y-1) not in visited and (x,y-1) not in dq:
            dq.append((x,y-1))
            grid[x][y-1]=grid[x][y]+1

        if y+1<M and grid[x][y+1]!=0  and (x,y+1) not in visited and (x,y+1) not in dq:
            dq.append((x,y+1))
            grid[x][y+1]=grid[x][y]+1


sol()