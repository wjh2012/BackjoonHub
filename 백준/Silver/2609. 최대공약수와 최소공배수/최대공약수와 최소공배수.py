def gcd(a,b):
    if b==0:
        return a
    return(gcd(b,a%b))

def lcm(a,b):
    return a*b//gcd(a,b)

x,y = map(int,input().split())
print(gcd(max(x,y),min(x,y)))
print(lcm(max(x,y),min(x,y)))