import sys

def sol():
    N = int(sys.stdin.readline())
    a = []
    for _ in range(N):
        a.append(list(map(int,sys.stdin.readline().split())))

    for i in range(1, N):
        a[i][0]+=min(a[i-1][1],a[i-1][2])
        a[i][1]+=min(a[i-1][0],a[i-1][2])
        a[i][2]+=min(a[i-1][0],a[i-1][1])
    print(min(a[-1]))

sol()