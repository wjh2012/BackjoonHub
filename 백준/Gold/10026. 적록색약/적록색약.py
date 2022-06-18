import sys

def sol():
    N=int(input())
    grid=[]
    for _ in range(N):
        grid.append(list(sys.stdin.readline().rstrip()))

    mx=[1,-1,0,0]
    my=[0,0,1,-1]

    visited=[]
    ans = 0
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                dq=[]
                dq.append((i,j))
                while dq:
                    (x,y)=dq.pop()
                    visited.append((x,y))
                    color = grid[x][y]

                    for k in range(4):
                        nx = x+mx[k]
                        ny = y+my[k]
                        
                        if nx<0 or nx==N or ny<0 or ny==N:
                            continue

                        if (nx,ny) not in visited and grid[nx][ny]==color:
                            dq.append((nx,ny))
                ans+=1

    visited=[]
    ans2 = 0
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                dq=[]
                dq.append((i,j))
                while dq:
                    (x,y)=dq.pop()
                    visited.append((x,y))
                    color = grid[x][y]

                    for k in range(4):
                        nx = x+mx[k]
                        ny = y+my[k]
                        
                        if nx<0 or nx==N or ny<0 or ny==N:
                            continue
                        
                        if (nx,ny) not in visited:
                            if color=='B' and  grid[nx][ny]==color:
                                dq.append((nx,ny))
                            elif color!='B' and grid[nx][ny]!='B':
                                dq.append((nx,ny))
                ans2+=1

    print(ans,ans2)
sol()