from collections import deque, defaultdict
import sys

def sol():
    N = int(sys.stdin.readline())
    dic = defaultdict(list)
    for _ in range(N-1):
        a,b=map(int,sys.stdin.readline().split())
        dic[a].append(b)
        dic[b].append(a)

    dq = deque([1])
    visited = [0]*(N+1)

    while dq:
        x = dq.popleft()
        for i in dic[x]:
            if not visited[i]:
                dq.append(i)
                visited[i]=x

    print(*visited[2:],sep='\n')

sol()