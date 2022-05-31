n = int(input())
l = []
for _ in range(n):
    l.append(tuple(map(int,input().split())))
l.sort(key=lambda x:x[0])
l.sort(key=lambda x:x[1])
for i,j in l:
    print(i,j)