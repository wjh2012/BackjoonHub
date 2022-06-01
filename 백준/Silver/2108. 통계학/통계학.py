import sys
from collections import defaultdict

n=int(sys.stdin.readline())

a=[]
b=defaultdict(int)

for _ in range(n):
    num = int(sys.stdin.readline())
    a.append(num)
    b[num]+=1
    
a.sort()
#산술평균    
print(round(sum(a)/n))

#중앙값
print(a[n//2])

#최빈값
maximum = max(b.values())
alist = [x for x,y in b.items() if y==maximum]
if len(alist)==1:
    print(alist[0])
else:
    print(sorted(alist)[1])

#범위
print(a[-1]-a[0])