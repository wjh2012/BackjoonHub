import sys

def sol():
    dp = [[[1]*21 for _ in range(21)] for _ in range(21)]
    for a in range(1,21):
        for b in range(1,21):
            for c in range(1,21):
                if a < b < c:
                    dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
                else:
                    dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

    

    while True:
        a,b,c = map(int,sys.stdin.readline().split())
        if a==-1 and b==-1 and c==-1:
            return
        else:
            ans = 0

            if a <= 0 or b <= 0 or c <= 0:
                ans = 1
            elif a > 20 or b > 20 or c > 20:
                ans = dp[20][20][20]
            else:
                ans = dp[a][b][c]

            print(f"w({a}, {b}, {c}) = {ans}")
        
sol()
