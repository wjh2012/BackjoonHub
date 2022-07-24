def sol():
    n = int(input())
    # 1000000007

    fib = [[1,1],[1,0]]

    def mprod(a,b):
        result = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += a[i][k]*b[k][j]

        for i in range(2):
            for j in range(2):
                result[i][j]=result[i][j]%1000000007
        return result

    def pow(n):
        if n==1:
            return fib

        x = pow(n//2)

        if n%2==0:
            return mprod(x,x)
        else:
            return mprod(mprod(x,x),fib)

    print(pow(n)[0][1])

sol()