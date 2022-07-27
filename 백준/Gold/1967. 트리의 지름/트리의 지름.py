import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

def sol():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n-1):
        a,b,c = map(int,sys.stdin.readline().split())
        tree[a].append((b,c))
    
    global ans
    ans = 0
    def dfs(n, accum):
        global ans
        node = tree[n]
        # 말단 노드
        if len(node)==0:
            return accum
        # 자식 노드 1개
        elif len(node)==1:
            return dfs(node[0][0], accum + node[0][1])
        # 자식노드 2개
        else:
            first = 0
            second = 0
            for child, wei in node:
                tmp = dfs(child, wei)
                if tmp>second:
                    if tmp>first:
                        first, second = tmp, first
                    else:
                        second = tmp

            inner = first + second
            choice = first + accum
            
            ans = max(ans, inner)
            return choice
            
    dfs(1,0)
    print(max(dfs(1,0),ans))

sol()