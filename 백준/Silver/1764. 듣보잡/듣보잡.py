import sys

def sol():
    n,m=map(int,sys.stdin.readline().split())
    
    duedo=set()
    bodo=set()

    for _ in range(n):
        duedo.add(sys.stdin.readline().rstrip())
    for _ in range(m):
        bodo.add(sys.stdin.readline().rstrip())
    
    db = duedo & bodo
    db=sorted(list(db))

    print(len(db))
    for i in db:
        print(i)

sol()