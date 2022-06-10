import sys
sys.setrecursionlimit(10**6)

def divide(arr,t,b,l,r):
    global blue, white
    n=b-t+1
    # 4 7 4 7
    good = n**2
    s = 0
    for i in range(t, t+n):
        s+=sum(arr[i][l:l+n])

    if s==0:
        white+=1
        return

    elif s==good:
        blue+=1
        return

    else:
        if good==4:
            white+=(4-s)
            blue += s
            return
        else:
            # 1
           #print(t, t+n//2-1, l, l+n//2-1)
            divide(arr, t, t+n//2-1, l, l+n//2-1)
            # 2     
            #print(t, t+n//2-1, l+n//2, l+n//2+n//2-1)
            divide(arr, t, t+n//2-1, l+n//2, l+n//2+n//2-1)
            # 3
            #print(t+n//2, t+n//2+1, l, l+n//2-1)
            divide(arr, t+n//2, t+n//2+n//2-1, l, l+n//2-1)
            # 4
            #print(t+n//2, t+n//2+1, l+n//2, l+n//2+n//2-1)
            divide(arr, t+n//2, t+n//2+n//2-1, l+n//2, l+n//2+n//2-1)

    

def sol():
    n = int(sys.stdin.readline())
    a=[]
    for _ in range(n):
        x = list(map(int,sys.stdin.readline().split()))
        a.append(x)

    global blue
    global white
    blue, white = 0, 0

    divide(a,0,n-1,0,n-1)
    print(white)
    print(blue)

    
sol()