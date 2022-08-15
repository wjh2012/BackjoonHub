import sys

def sol():
    N,M = map(int,sys.stdin.readline().split())
    grid = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    
    for i in range(1,N):
        grid[i][0] += grid[i-1][0]
    for j in range(1,M):
        grid[0][j] += grid[0][j-1]

    for i in range(1,N):
        for j in range(1,M):
            grid[i][j] +=  max(grid[i][j-1], grid[i-1][j], grid[i-1][j-1])

    print(grid[-1][-1])

sol()