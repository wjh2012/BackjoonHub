import sys
from collections import deque, defaultdict

def sol():
    N,K = map(int,sys.stdin.readline().split())
    
    dic = defaultdict(int)
    
    dic[N]=0
    dq = deque()
    dq.append(N)

    while dq:
        n = dq.popleft()

        if n==K:
            print(dic[n])
            break

        if 0<=n*2<=200000 and n*2 not in dic:
            dic[n*2]=dic[n]+1
            dq.append(n*2)
        if 0<=n+1<=100000 and n+1 not in dic:
            dic[n+1]=dic[n]+1
            dq.append(n+1)
        if 0<=n-1<=100000 and n-1 not in dic:
            dic[n-1]=dic[n]+1
            dq.append(n-1)

sol()