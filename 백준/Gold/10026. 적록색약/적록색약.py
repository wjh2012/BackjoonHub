import sys

def sol():
    N=int(input())
    grid=[]
    grid.append([0]*(N+2))
    for _ in range(N):
        grid.append([0]+list(sys.stdin.readline().rstrip())+[0])
    grid.append([0]*(N+2))

    mx=[1,-1,0,0]
    my=[0,0,1,-1]

    grid2 = [x.copy() for x in grid]
    
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if grid[i][j]:
                dq=[]
                dq.append((i,j))
                while dq:
                    (x,y)=dq.pop()
                    color = grid[x][y]
                    grid[x][y]=0

                    for k in range(4):
                        nx = x+mx[k]
                        ny = y+my[k]

                        if grid[nx][ny]==0 or (nx,ny) in dq or grid[nx][ny]!=color:
                            continue

                        dq.append((nx,ny))
                ans+=1

    ans2 = 0
    for i in range(N+2):
        for j in range(N+2):
            if grid2[i][j]:
                dq=[]
                dq.append((i,j))
                while dq:
                    (x,y)=dq.pop()
                    color = grid2[x][y]
                    grid2[x][y]=0

                    for k in range(4):
                        nx = x+mx[k]
                        ny = y+my[k]

                        if grid2[nx][ny]==0 or (nx,ny) in dq:
                            continue
                        if color=='B'and grid2[nx][ny]!='B':
                            continue
                        if color!='B' and grid2[nx][ny]=='B':
                            continue
                        dq.append((nx,ny))
                ans2+=1

    print(ans,ans2)
sol()