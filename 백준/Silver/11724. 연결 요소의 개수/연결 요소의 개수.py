import sys
from collections import defaultdict, deque

def sol():
    N,M=map(int,sys.stdin.readline().split())
    graph=defaultdict(set)

    # 그래프 생성
    for _ in range(M):
        a,b=map(int,sys.stdin.readline().split())
        graph[a].add(b)
        graph[b].add(a)

    noconnect = N-len(graph)

    ans=0
    while graph:
        node=list(graph.keys())[0]
        # BFS
        dq=deque([node])
        visited=[]
        while dq:
            n = dq.popleft()
            visited.append(n)
            for i in graph[n]:
                if i not in visited and i not in dq:
                    dq.append(i)
            del graph[n]
        ans+=1
    print(ans+noconnect)

sol()