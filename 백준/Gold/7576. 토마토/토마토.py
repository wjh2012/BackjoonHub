import sys
from collections import deque

def sol():
    M,N = map(int,sys.stdin.readline().split())
    box=[]
    for _ in range(N):
        box.append(list(map(int,sys.stdin.readline().split())))

    riped=deque()
    empty=0
    # 이미 익어있는 토마토
    for n in range(N):
        for m in range(M):
            if box[n][m]==1:
                riped.append((n,m))
            elif box[n][m]==-1:
                empty+=1
    
    day=deque()
    count=0
    visited = 0
    visited += len(riped)

    while riped:
        day=riped.copy()
        riped.clear()

        while day:
            i,j = day.popleft()

            # 위
            if 0<i and (i-1, j) and box[i-1][j]==0:
                box[i-1][j]=1
                visited+=1
                riped.append((i-1, j))
            # 아래
            if i<N-1 and (i+1, j) and box[i+1][j]==0:
                box[i+1][j]=1
                visited+=1
                riped.append((i+1, j))
            # 왼쪽
            if 0<j and (i, j-1) and box[i][j-1]==0:
                box[i][j-1]=1
                visited+=1
                riped.append((i, j-1))
            # 오른쪽
            if j<M-1 and (i, j+1) and box[i][j+1]==0:
                box[i][j+1]=1
                visited+=1
                riped.append((i, j+1))

        count+=1
    if M*N-empty == visited:
        print(count-1)
    else:
        print(-1)

sol()
