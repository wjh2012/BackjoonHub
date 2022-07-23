import sys

def sol():
    n = int(input())
    m = int(input())

    tt=[[9999999999]*n for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        if tt[a-1][b-1]==0 or tt[a-1][b-1]>c:
            tt[a-1][b-1]=c

    for way in range(n):
        for start in range(n):
            for end in range(n):
                tt[start][end] = min(tt[start][end], tt[start][way]+tt[way][end])
                    

    for i in range(n):
        for j in range(n):
            if i==j or tt[i][j]==9999999999:
                print(0, end = ' ')
            else:
                print(tt[i][j], end=' ')
        print()

sol()