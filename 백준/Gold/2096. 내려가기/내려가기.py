import sys

def sol():
    N = int(sys.stdin.readline())
    a,b,c = 0,0,0
    x,y,z = 0,0,0
    for i in range(N):
        A,B,C = map(int,sys.stdin.readline().split())
        if i==0:
            x,y,z = a,b,c = A,B,C
            continue
        a,b,c = A + max(a,b), B + max(a,b,c), C + max(b,c)
        x,y,z = A + min(x,y), B + min(x,y,z), C + min(y,z)

    print(max(a,b,c), min(x,y,z))

sol()
