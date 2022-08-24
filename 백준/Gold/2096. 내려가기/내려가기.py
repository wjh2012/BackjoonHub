import sys

def sol():
    N = int(sys.stdin.readline())
    a,b,c =  map(int,sys.stdin.readline().split())
    x,y,z = a,b,c
    for _ in range(1,N):
        A,B,C = map(int,sys.stdin.readline().split())
        a,b,c = A + max(a,b), B + max(a,b,c), C + max(b,c)
        x,y,z = A + min(x,y), B + min(x,y,z), C + min(y,z)

    print(max(a,b,c), min(x,y,z))

sol()
