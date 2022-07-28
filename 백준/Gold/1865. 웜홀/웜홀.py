import sys
from collections import defaultdict,deque
INF = 9999999999999
def sol():
    TC = int(input())
    for _ in range(TC):
        N,M,W = map(int,sys.stdin.readline().split())
        graph = []
        for _ in range(M):
            S,E,T = map(int,sys.stdin.readline().split())
            graph.append((S,E,T))
            graph.append((E,S,T))
        for _ in range(W):
            S,E,T = map(int,sys.stdin.readline().split())
            graph.append((S,E,-T))
        
        def bf():
            tt = [INF] * (N+1)
            tt[1] = 0
            
            for i in range(N):
                for s,e,t in graph:
                    if tt[e] > tt[s] + t:
                        tt[e] = tt[s] + t
                        if i == N-1:
                            return True
            return False
        
        if bf():
            print('YES')
        else:
            print('NO')
                        
                    
sol()