import sys
from collections import deque

def sol():
    M,N,H = map(int,sys.stdin.readline().split())
    box=[[list(map(int,sys.stdin.readline().split()))for _ in range(N)]for _ in range(H)]
    
    stack = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x]==1:
                    stack.append((z,y,x))

    dx=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dz=[0,0,0,0,1,-1]
    
    while stack:
        z,y,x = stack.popleft()
        
        for i in range(6):
            nz=z+dz[i]
            if nz<0 or nz>H-1:
                continue

            ny=y+dy[i]
            if ny<0 or ny>N-1:
                continue

            nx=x+dx[i]
            if nx<0 or nx>M-1:
                continue

            if box[nz][ny][nx]==0:
                stack.append((nz,ny,nx))
                box[nz][ny][nx]=box[z][y][x]+1

    maxx=1
    for z in box:
        for y in z:
            for x in y:
                if x==0:
                    print(-1)
                    return
                maxx=max(maxx,x)

    print(maxx-1)
            
sol()