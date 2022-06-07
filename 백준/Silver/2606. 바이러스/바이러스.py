import sys
from collections import defaultdict, deque

def sol():
    n=int(sys.stdin.readline())
    e=int(sys.stdin.readline())
    net=defaultdict(list)

    # 그래프 생성
    for _ in range(e):
        a,b=map(int,sys.stdin.readline().split())
        if b not in net[a]:
            net[a].append(b)
        if a not in net[b]:
            net[b].append(a)

    # BFS
    dq=deque([1])
    visited=[]
    ans=0
    while dq:
        n = dq.popleft()
        ans+=1
        visited.append(n)
        for i in net[n]:
            if i not in visited and i not in dq:
                dq.append(i)
    print(ans-1)
sol()