import sys

def sol():
    N = int(sys.stdin.readline())
    tri = []
    for _ in range(N):
        tri.append(list(map(int,sys.stdin.readline().split())) )

    if N==1:
        print(*tri[0])
        return

    for i in range(1,N):
        tri[i][0]+=tri[i-1][0]
        for j in range(1,i):
            tri[i][j]+=max(tri[i-1][j-1],tri[i-1][j])
        tri[i][i]+=tri[i-1][i-1]

    print(max(tri[-1]))
    
sol()