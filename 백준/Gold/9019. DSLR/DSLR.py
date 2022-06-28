import sys
from collections import deque

def sol():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        A,B = map(int,sys.stdin.readline().split())
        visited = ['']*10001

        visited[A]=' '
        dq=deque([A])

        while dq:
            n = dq.popleft()
            if n==B:
                print(visited[n].lstrip())
                break
            # D
            D = (n*2)%10000
            if not visited[D]:
                visited[D] = visited[n]+'D'
                dq.append(D)
            # S
            if n==0:
                S=9999
            else:
                S=n-1
            if not visited[S]:
                visited[S] = visited[n]+'S'
                dq.append(S)
            # L
            a=n//1000
            b=(n-a*1000)//100
            c=(n-a*1000-b*100)//10
            d=n%10

            L = a+b*1000+c*100+d*10
            if not visited[L]:
                visited[L] = visited[n]+'L'
                dq.append(L)
            # R
            a=n//1000
            b=(n-a*1000)//100
            c=(n-a*1000-b*100)//10
            d=n%10

            R = a*100 + b*10 + c + d*1000
            if not visited[R]:
                visited[R] = visited[n]+'R'
                dq.append(R)
sol()