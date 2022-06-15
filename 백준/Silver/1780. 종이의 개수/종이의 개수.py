import sys

def recurs(a, n, cur):
    x=cur[0]
    y=cur[1]

    if n==1:
        dic[a[x][y]]+=1
        return

    flag = a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if flag!=a[i][j]:
                flag=a[i][j]
                break
        if flag!=a[x][y]:
            break

    if flag!=a[x][y]:
        for i in range(x,x+n,n//3):
            for j in range(y,y+n,n//3):
                recurs(a, n//3, (i,j))
    else:
        dic[flag]+=1
                
def sol():
    N = int(sys.stdin.readline())
    a=[]
    for _ in range(N):
        a.append(list(map(int,sys.stdin.readline().split())))
    
    global dic
    dic={
        -1:0,
        0:0,
        1:0
    }

    recurs(a,N,(0,0))

    for i in dic.values():
        print(i)

sol()