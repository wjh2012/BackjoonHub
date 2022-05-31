from collections import deque

n = int(input())
dq = deque()

for i in range(n):
    dq.append(i+1)

while dq:
    if len(dq)==1:
        print(dq[0])
        break
    dq.popleft()
    dq.append(dq.popleft())