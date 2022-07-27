import sys
from collections import deque

def sol():
    N, M = map(int,input().split())
    grid = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
    wall = [[[0,0] for _ in range(M)] for _ in range(N)]
    wall[0][0][0]=1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    dq = deque([(0,0,0)])
    while dq:
        x,y,z = dq.popleft()
        if x==N-1 and y == M-1:
            print(wall[x][y][z])
            return

        for i in range(4):
            nx = x+dx[i]
            if nx > N-1 or nx < 0:
                continue
            ny = y+dy[i]
            if ny > M-1 or ny < 0:
                continue
            
            # 벽이고, 부술 기회가 있다면
            if grid[nx][ny] == 1 and z == 0:
                wall[nx][ny][1] = wall[x][y][0]+1
                dq.append((nx,ny,1))

            elif grid[nx][ny] == 0 and wall[nx][ny][z]==0:
                wall[nx][ny][z] = wall[x][y][z]+1
                dq.append((nx,ny,z))

    print(-1)

sol()