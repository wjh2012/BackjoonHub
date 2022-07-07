def pow(A,B,C):
    if B==0:
        return 1
    
    x=pow(A,B//2,C)

    if B%2==0:
        return x*x%C
    else:
        return A*x*x%C


def sol():
    A,B,C = map(int,input().split())
    print(pow(A,B,C))

sol()