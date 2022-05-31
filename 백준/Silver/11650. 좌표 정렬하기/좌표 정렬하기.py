import sys
n=int(sys.stdin.readline())
ans=[]
for _ in range(n):
    ans.append(tuple(map(int,sys.stdin.readline().split())))
ans.sort(key=lambda x:x[1])
ans.sort(key=lambda x:x[0])        
for x, y in ans:
    print(x, y)