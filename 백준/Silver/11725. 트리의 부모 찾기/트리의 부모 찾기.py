from collections import deque, defaultdict

def sol():
    N = int(input())
    dic = defaultdict(list)
    for _ in range(N-1):
        a,b=map(int,input().split())
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

    for i in range(2,N+1):
        print(visited[i])

sol()