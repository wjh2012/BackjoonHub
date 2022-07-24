def sol():
    A = int(input())
    X = int(input())
    D = 1000000007

    def pow(a,n,d):
        if n==1:
            return a%d

        x = pow(a, n//2,d)

        if n%2==0:
            return (x*x)%d
        else:
            return (x*x*a)%d

    print(pow(A,X,D))

sol()