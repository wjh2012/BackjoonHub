import sys
def sol():
    N = int(sys.stdin.readline())
    if N==1:
        print(1)
        return
    a=1
    b=2
    for _ in range(N-2):
        a,b=b,(a+b)%15746
    print(b)
sol()