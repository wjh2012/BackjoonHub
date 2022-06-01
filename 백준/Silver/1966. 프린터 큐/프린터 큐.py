import sys
from collections import deque

t=int(input())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    a = deque(map(lambda x,y:(x,int(y)),[x for x in range(n)],sys.stdin.readline().split()))
  
    count=0

    while True:
        if a[0][1]==max(a,key=lambda x:x[1])[1]:
            if a[0][0]==m:
                print(count+1)
                break
            count+=1
            a.popleft()
        else:
            a.rotate(-1)