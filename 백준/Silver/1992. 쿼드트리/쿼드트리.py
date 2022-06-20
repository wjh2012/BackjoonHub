import sys

def sq(a,n,x,y):
    global ans

    ini = a[x][y]
    flag = False
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[i][j]!=ini:
                flag = True
                break
        if flag:
            break

    if flag:
        if n==2:
            ans+='('
            ans+=str(a[x][y])
            ans+=str(a[x][y+1])
            ans+=str(a[x+1][y])
            ans+=str(a[x+1][y+1])
            ans+=')'
            return

        ans+='('
        nn = n//2
        sq(a,nn,x,y)
        sq(a,nn,x,y+nn)
        sq(a,nn,x+nn,y)
        sq(a,nn,x+nn,y+nn)
        ans+=')'
        return
    else:
        ans+=str(ini)

def sol():
    N = int(input())
    a = [list(map(int,sys.stdin.readline().rstrip()))for _ in range(N)]
    
    global ans
    ans =""

    sq(a,N,0,0)

    print(ans)

sol()