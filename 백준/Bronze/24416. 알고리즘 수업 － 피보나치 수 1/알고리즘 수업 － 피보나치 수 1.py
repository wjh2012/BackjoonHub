def dpf(n):
    d=[2,3]+[0]*(n-1)
    for i in range(2,n-2):
        d[i]=d[i-2]+d[i-1]
    return d[i]


n=int(input())

print(dpf(n),n-2)