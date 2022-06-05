import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

seta = set(a)
aa = sorted(list(seta))

dic = {}

for i in range(len(aa)):
    dic[aa[i]]=i

ans = []
for i in a:
    ans.append(dic[i])

print(*ans)