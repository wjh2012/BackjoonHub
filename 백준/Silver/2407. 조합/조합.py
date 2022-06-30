def sol():
    n,m=map(int,input().split())
    pac = [0]*(n+1)
    pac[1]=1
    for i in range(2,n+1):
        pac[i]=pac[i-1]*i
    
    print(pac[n]//pac[n-m]//pac[m])

sol()