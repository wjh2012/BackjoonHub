import sys

k = int(sys.stdin.readline())
num = list(map(int,sys.stdin.read().split()))
ans=[]

for i in num:
    if i==0:
        ans.pop()
    else:
        ans.append(i)
        
print(sum(ans))