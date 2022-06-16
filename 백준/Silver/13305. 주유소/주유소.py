import sys

def sol():
    N = int(sys.stdin.readline())-1
    road=list(map(int,sys.stdin.readline().split()))
    price=list(map(int,sys.stdin.readline().split()))
    price.pop()

    for i in range(N-2,-1,-1):
        road[i]=road[i]+road[i+1]

    total = road[0]
    ans = 0
    went=0
    while total>0:
        idx = price.index(min(price))
        end = road[idx]-went
        if total>end:
            went+=end
            total-=end
            ans+=end*price[idx]
        else:
            ans+=total*price[idx]
            total=0
            continue
        del price[idx:]
        
    print(ans)

sol()