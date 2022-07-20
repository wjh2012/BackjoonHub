import sys

def sol():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    
    grid = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                grid[i][j] = grid[i-1][j-1]+1
            else:
                grid[i][j] = max(grid[i][j-1], grid[i-1][j])
    
    print(grid[-1][-1])

sol()