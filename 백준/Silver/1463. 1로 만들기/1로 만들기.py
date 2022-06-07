def sol():
    n=int(input())
    a=[0]*(n+1)
    a[1]=0

    for i in range(2,n+1):
        t=[]
        # 1뺀 경우
        t.append(a[i-1]+1)
        # 2와 3 모두 나누어질 경우
        if i%6==0:
            t.append(a[i//2]+1)
            t.append(a[i//3]+1)
        # 2로만 나누어질 경우
        elif i%2==0:
            t.append(a[i//2]+1)
        # 3으로만 나누어질 경우
        elif i%3==0:
            t.append(a[i//3]+1)

        a[i]=min(t)
        
    print(a[n])

sol()