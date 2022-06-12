import sys

def sol():
    N=int(sys.stdin.readline())
    grid=[[0]*(N+2)]
    for _ in range(N):
        grid.append([0]+list(map(int,sys.stdin.readline().rstrip()))+[0])
    grid.append([0]*(N+2))

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    answer=[]

    for n in range(N+2):
        for m in range(N+2):
            if grid[n][m]:
                dq=[]
                dq.append((n,m))
                grid[n][m]=0

                count=0
                while dq:
                    x,y=dq.pop()
                    count+=1
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y+dy[i]
            
                        if grid[nx][ny]==0:
                            continue

                        if grid[nx][ny]==1:
                            dq.append((nx,ny))
                            grid[nx][ny]=0

                answer.append(count)
                
    print(len(answer))
    print(*sorted(answer),sep='\n')

sol()