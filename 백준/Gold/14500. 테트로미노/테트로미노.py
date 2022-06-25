import sys

def dfs(x,y,depth,sum_val):
    global N,M,max_val,paper,check

    if depth==4:
        max_val=max(max_val,sum_val)
        return

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>N-1 or ny<0 or ny>M-1:
            continue

        if check[nx][ny]:
            check[nx][ny]=False
            dfs(nx,ny,depth+1,sum_val+paper[nx][ny])
            check[nx][ny]=True

def around(x,y):
    global N,M,paper
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    s=paper[x][y]
    cros=[]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>N-1 or ny<0 or ny>M-1:
            continue
        cros.append(paper[nx][ny])

    if len(cros) >=3:
        cros.sort(reverse=True)
        return sum(cros[0:3])+s
    else:
        return 0
        
def sol():
    global N,M,max_val,paper,check
    max_val=0
    N,M = map(int,sys.stdin.readline().split())
    paper=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]
    check=[[True]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            check[i][j]=False
            dfs(i,j,1,paper[i][j])
            check[i][j]=True
            max_val = max(max_val,around(i,j))

    print(max_val)

sol()