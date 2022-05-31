from collections import deque

n = int(input())
comm=[]
for _ in range(n):
    comm.append(input())

dq=deque()
        
        
for com in comm:
    if com.startswith('push'):
        com=com.split()
        if com[0]=='push_front':
            dq.appendleft(com[1])
        else:
            dq.append(com[1])
    else:
        if com=='pop_front':
            print(dq.popleft() if dq else -1)
        elif com=='pop_back':
            print(dq.pop() if dq else -1)
        elif com=='size':
            print(len(dq))
        elif com=='empty':
            print(1 if not dq else 0)
        elif com=='front':
            print(dq[0] if dq else -1)
        elif com=='back':
            print(dq[-1] if dq else -1)