import sys
from collections import deque

def sol():
    T = int(sys.stdin.readline())

    for i in range(T):
        p = list(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline())
        x = sys.stdin.readline().rstrip()

        x = x.replace('[','').replace(']','')

        if p.count('D')>n:
            print('error')

        elif n==0:
            print('[]')

        else:
            x=list(map(int,x.split(',')))

            x=deque(x)
            flag=True
            for comm in p:
                if comm=='R':
                    flag=not flag
                else:
                    if flag:
                        x.popleft()
                    
                    else:
                        x.pop()
            if not flag:
                x.reverse()

            print('[',end='')
            print(*x,sep=',',end='')
            print(']')

sol()        
        