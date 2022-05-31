import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(int)

for _ in range(n):
    dic[int(sys.stdin.readline())]+=1

for i in range(10000+1):
    while dic[i]:
        print(i)
        dic[i]-=1