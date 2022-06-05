def rec(n,r,c):
    global count

    if n==0:
        return

    i = r//(2**(n-1))
    j = c//(2**(n-1))
    if i:
        if j:# 4사분면(4)
            count+=(4**(n-1))*3
            r-=2**(n-1)
            c-=2**(n-1)
        else:# 3사분면(3)
            count+=(4**(n-1))*2
            r-=2**(n-1)
    else:
        if j:# 1사분면(2)
            count+=(4**(n-1))
            c-=2**(n-1)
        else:# 2사분면(1)
            pass

    return rec(n-1,r,c)

def sol():
    N,r,c = map(int,input().split())
    global count
    count=0

    rec(N,r,c)
    print(count)

sol()