import sys
from collections import deque

def sol():
    a = []
    B,R,L =(0,0),(0,0),(0,0)
    for i in range(10):
        j = list(sys.stdin.readline().rstrip())
        if 'B' in j:
            B=(i,j.index('B'))
        if 'R' in j:
            R=(i,j.index('R'))
        if 'L' in j:
            L=(i,j.index('L'))
        a.append(j)

    dq=deque()
    dq.append((L[0],L[1],0))
    visited=[]
    
    while dq:
        x, y, c = dq.popleft()
        visited.append((x,y))

        if (x,y) == B:
            print(c-1)
            break

        # 상
        if x>0 and (x-1,y)!=R and (x-1,y) not in visited and (x-1,y,c+1) not in dq:
            dq.append((x-1,y,c+1))
        # 하
        if x<10 and (x+1,y)!=R and (x+1,y) not in visited and (x+1,y,c+1) not in dq:
            dq.append((x+1,y,c+1))
        # 좌
        if y>0 and (x,y-1)!=R and (x,y-1) not in visited and (x,y-1,c+1) not in dq:
            dq.append((x,y-1,c+1))
        # 우
        if y<10 and (x,y+1)!=R and (x,y+1) not in visited and (x,y+1,c+1) not in dq:
            dq.append((x,y+1,c+1))
        

sol()