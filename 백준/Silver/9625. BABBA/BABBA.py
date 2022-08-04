import sys
def sol():
    N = int(sys.stdin.readline())
    if N==1:
        print(0,1)
        return
    a=1
    b=1
    for _ in range(N-2):
        a,b=b,(a+b)
    print(a,b)
sol()