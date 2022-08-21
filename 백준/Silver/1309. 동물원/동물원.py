import sys

def sol():
    N = int(sys.stdin.readline())
    
    if N==1:
        print(3)
        return

    a,b=3,7    
    for _ in range(N-2):
        a,b = b,a+b*2
    print(b%9901)

sol()
