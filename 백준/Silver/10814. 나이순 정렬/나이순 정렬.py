import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(tuple(sys.stdin.readline().split()))

arr.sort(key=lambda x:int(x[0]))

for i,j in arr:
    print(i,j)