def sol():
    t=int(input())

    for _ in range(t):
        n=int(input())
        if n==0:
            print(0)
        elif n==1:
            print(1)
        elif n==2:
            print(2)
        elif n==3:
            print(4)
        else:
            a=[]
            a=[0]*(n+1)
            a[1]=1
            a[2]=2
            a[3]=4

            for i in range(4,n+1):
                a[i]=a[i-1]+a[i-2]+a[i-3]

            print(a[n])
sol()
