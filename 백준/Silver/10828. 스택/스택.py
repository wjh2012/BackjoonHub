import sys

n = int(sys.stdin.readline())

dq=[]
for _ in range(n):
    com=sys.stdin.readline().rstrip()
    if com.startswith('push'):
        com=com.split()
        dq.append(com[1])
    else:
        if com=='pop':
            print(dq.pop() if dq else -1)
        elif com=='size':
            print(len(dq))
        elif com=='empty':
            print(1 if not dq else 0)
        elif com=='top':
            print(dq[-1] if dq else -1)