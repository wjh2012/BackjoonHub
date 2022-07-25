import sys
import heapq
from collections import defaultdict

INF = 400000

def sol():
    V, E = map(int,sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    
    G = defaultdict(list)
    for _ in range(E):
        u,v,w = map(int,sys.stdin.readline().split())
        G[u].append((v,w))

    K_route = [INF]*(V+1)
    K_route[K] = 0

    heap=[(K_route[K], K)]
    while heap:
        cur_w, node = heapq.heappop(heap)
        if cur_w > K_route[node]:
            continue
        for v,w in G[node]:
            pass_w = cur_w + w
            if K_route[v] > pass_w:
                K_route[v] = pass_w
                heapq.heappush(heap, (pass_w, v))

    for a in K_route[1:]:
        if a==INF:
            print('INF')
        else:
            print(a)

sol()