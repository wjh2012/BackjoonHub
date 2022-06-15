import sys

def sol():
    N=int(sys.stdin.readline())
    a=[]
    for _ in range(N):
        a.append(list(map(int,sys.stdin.readline().split())))

    for i in range(N):
        dq=[]
        for j in range(N):
            if a[i][j]==1:
                dq.append(j)
                while dq:
                    t = dq.pop()
                    for k in range(N):
                        if a[t][k]==1 and a[i][k]==0:
                            a[i][k]=1
                            dq.append(k)
    for i in a:
        print(*i)
sol()