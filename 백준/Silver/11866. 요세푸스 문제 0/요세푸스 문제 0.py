import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

dq=deque()
ans=[]

for i in range(n):
    dq.append(i+1)

while dq:
    dq.rotate(-(k-1))
    ans.append(dq.popleft())
print('<',end='')
print(*ans,sep=', ',end='')
print('>',end='')