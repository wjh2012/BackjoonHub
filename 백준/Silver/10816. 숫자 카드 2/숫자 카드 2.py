import sys
from collections import defaultdict

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
    
aa=set(a)
bb=set(b)
cc = aa&bb

a = [x for x in a if x in cc]

dic = defaultdict(int)

for i in a:
    dic[i]+=1

for i in b:
    print(dic[i], end=' ')