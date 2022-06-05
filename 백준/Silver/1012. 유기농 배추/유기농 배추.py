import sys
from collections import deque

t = int(sys.stdin.readline())

def makeGraph(field, x,y):
    for key in field.keys():
        if (abs(key[0]-x)+abs(key[1]-y))==1:
            field[key].append((x,y))
            field[(x,y)].append((key[0],key[1]))

def sol():
    for _ in range(t):
        m, n, k = map(int,sys.stdin.readline().split())
        field = {}
        for _ in range(k):
            x, y = map(int,sys.stdin.readline().split())

            field[(x,y)]=[]
            makeGraph(field,x,y)

        dq = deque()
        count=0

        while field:
            visited=[]
            start = list(field.keys())[0]
            dq.append(start)
            while dq:
                who = dq.popleft()
                visited.append(who)
                nearby = field[who]
                for cabbage in nearby:
                    if cabbage not in dq and cabbage not in visited:
                        dq.append(cabbage)
                del field[who]
            count+=1
        print(count)
sol()