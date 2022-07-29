import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

def sol():
    V = int(input())
    tree = defaultdict(list)
    for _ in range(V):
        a = list(map(int,sys.stdin.readline().rstrip('-1\n').split()))
        for i in range(len(a)//2):
            tree[a[0]].append((a[i*2+1],a[i*2+2]))
    
    global ans
    ans = 0
    global tmp
    tmp = 1
    def dfs(n,cumul,visited):
        global ans
        global tmp
        flag = True
        for node, val in tree[n]:
            if visited[node]:
                visited[node]=False
                dfs(node, cumul+val, visited)
                if flag:
                    flag = False
        if flag:
            if cumul>ans:
                ans = cumul
                tmp = n

    start = 1
    maximum = 0
    while True:
        visited = [True] * (V+1)
        visited[start]=False
        dfs(start,0,visited)
        
        if maximum == ans:
            print(ans)
            return
        else:
            maximum = ans
            start = tmp
        
sol()