def sol():
    N = int(input())
    global ans
    ans = 0

    a = [False]*N
    b = [False]*(2*N-1)
    c = [False]*(2*N-1)

    def dfs(x):
        global ans
        if x==N:
            ans+=1
            return
        
        for i in range(N):
            if not (a[i] or b[x+i] or c[x-i+N-1]):
                a[i] = b[x+i] = c[x-i+N-1] = True
                dfs(x+1)
                a[i] = b[x+i] = c[x-i+N-1] = False

    dfs(0)
    print(ans)
    
sol()