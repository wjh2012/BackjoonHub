import sys
n=int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

summ=0
for i in range(n):
    summ+=sum(a[:i+1])
print(summ)