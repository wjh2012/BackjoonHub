import sys

def sol():
    N,M=map(int,sys.stdin.readline().split())

    a=[[N]*N for _ in range(N)]

    for i in range(M):
        A,B = map(int,sys.stdin.readline().split())
        a[A-1][B-1]=1
        a[B-1][A-1]=1
    

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if a[i][j]>a[i][k]+a[k][j]:
                    a[i][j]=a[i][k]+a[k][j]
    
    ans = []
    for i in range(N):
        ans.append(sum(a[i]))
    mi = min(ans)
    for i in range(N):
        if ans[i]==mi:
            print(i+1)
            return

sol()