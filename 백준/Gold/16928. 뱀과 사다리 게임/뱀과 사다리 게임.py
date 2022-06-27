import sys
from collections import defaultdict, deque

def sol():
    N,M = map(int,sys.stdin.readline().split())
    visited = [0]*101
    event = defaultdict(int)

    for _ in range(N):
        x,y = map(int,sys.stdin.readline().split())
        event[x]=y
    for _ in range(M):
        u,v = map(int,sys.stdin.readline().split())
        event[u]=v

    dq = deque([1])
    while dq:
        cur = dq.popleft()

        if cur == 100:
            print(visited[cur])
            break

        for dice in range(1,7):
            nextLoc = cur+dice
            # 100 초과하면 스킵
            if nextLoc>100:
                continue
            
            # 이미 방문했고, 더 빠르면 스킵
            if 0<visited[nextLoc]<=visited[cur]+1:
                continue

            # 사다리칸 or 뱀칸 이면
            if event[nextLoc]:
                # 점프할 칸
                jumpLoc = event[nextLoc]
                
                # 이미 방문했고, 더 빠르면 스킵
                if 0<visited[jumpLoc]<visited[cur]+1:
                    continue
                
                visited[nextLoc]=visited[cur]+1
                visited[jumpLoc]=visited[cur]+1
                dq.append(jumpLoc)
            
            else:
                visited[nextLoc]=visited[cur]+1
                dq.append(nextLoc)
    
sol()