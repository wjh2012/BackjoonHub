import sys
from collections import deque
def sol():
    N = int(sys.stdin.readline())
    grid = []
    for _ in range(N):
        grid.append(list(map(int,sys.stdin.readline().split())))

    dq=deque()
    dq.append((0,0))
    visited = []
    while dq:
        x,y = dq.popleft()
        visited.append((x,y))
        val = grid[x][y]

        if y+val<N and (x,y+val) not in visited and (x,y+val) not in dq:
            dq.append((x,y+val))
        if x+val<N and (x+val,y) not in visited and (x+val,y) not in dq:
            dq.append((x+val,y))

    if (N-1,N-1) in visited:
        print('HaruHaru')
    else:
        print('Hing')

sol()