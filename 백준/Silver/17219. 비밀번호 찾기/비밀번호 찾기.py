import sys
n,m=map(int, sys.stdin.readline().split())
dic={}
for _ in range(n):
    site, pwd = sys.stdin.readline().split()
    dic[site]=pwd

for _ in range(m):
    s=sys.stdin.readline().rstrip()
    print(dic[s])