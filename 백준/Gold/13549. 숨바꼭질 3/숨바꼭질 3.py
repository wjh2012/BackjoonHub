import sys
from collections import deque

def sol():
    N,K = map(int,sys.stdin.readline().split())

    line = [0]*200001
    line[N]=1
    dq = deque([N])
    
    while dq:
        x = dq.popleft()
        if x==K:
            print(line[x]-1)
            break

        back = x-1
        front = x+1
        telpo = 2*x
        
        if 0 <= telpo < 200001 and line[telpo]==0:
            dq.append(telpo)
            line[telpo]=line[x]

        if 0 <= back < 200001 and line[back]==0:
            dq.append(back)
            line[back]=line[x]+1

        if 0 <= front < 200001 and line[front]==0:
            dq.append(front)
            line[front]=line[x]+1

sol()