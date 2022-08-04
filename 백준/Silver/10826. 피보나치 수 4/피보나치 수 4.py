import sys
def sol():
    N = int(sys.stdin.readline())
    a=0
    b=1
    for _ in range(N):
        a,b=b,(a+b)
    print(a)

sol()