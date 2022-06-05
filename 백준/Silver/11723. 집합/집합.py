import sys

m = int(sys.stdin.readline())

s = set()
for _ in range(m):
    co = sys.stdin.readline().rstrip()
    if ' ' in co:
        comm, n = co.split()
        n=int(n)
    else:
        comm=co

    if comm=='add':
        s.add(n)
    elif comm=='remove':
        if n in s:
            s.remove(n)
    elif comm=='check':
        if n in s:
            print(1)
        else:
            print(0)
    elif comm=='toggle':
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif comm=='all':
        s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif comm=='empty':
        s=set()