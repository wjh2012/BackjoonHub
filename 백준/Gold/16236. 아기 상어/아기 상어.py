import sys
from collections import deque

def nearest(shark):
    global N, sea, size, times, eat   

    check = [[0]*N for _ in range(N)]
    check[shark[0]][shark[1]]=1

    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    
    nearList=[]
    distance = 401
    dq=deque([shark])
    while dq:
        x,y = dq.popleft()
        if check[x][y]==distance:
            continue
        for i in range(4):
            nx = x+dx[i]
            if nx<0 or nx>N-1:
                continue
            ny = y+dy[i]
            if ny<0 or ny>N-1:
                continue
            if sea[nx][ny]>size:
                continue
            if check[nx][ny]:
                continue

            check[nx][ny]=check[x][y]+1
            if 0<sea[nx][ny]<size:
                distance=check[nx][ny]
                nearList.append((nx,ny))
            else: 
                dq.append((nx,ny))
    if nearList:
        nearList.sort(key=lambda x:x[1])
        nearList.sort(key=lambda x:x[0])
        times+=distance-1
        return nearList[0]
    else:
        return False

def sol():
    global N, sea, size, times, eat
    size=2
    times=0
    eat=0

    N = int(input())
    sea = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
    

    shark=None
    for i in range(N):
        for j in range(N):
            if sea[i][j]==9:
                shark = (i,j)
                sea[i][j]=0
                break
        if shark:
            break
    
    while True:
        shark = nearest(shark)
        if not shark:
            break
        x,y = shark
        sea[x][y]=0
        eat+=1
        if eat==size:
            eat=0
            size+=1

    print(times)
    
sol()   