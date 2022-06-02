import sys

def sol():
    n=int(sys.stdin.readline())
    
    num = [x for x in range(n,0,-1)]
    stac=[]
    ans=[]
    for _ in range(n):
        a=int(sys.stdin.readline())

        while num or stac:
            if num and num[-1]<=a:
                stac.append(num.pop())
                ans.append('+')

            else:
                if stac[-1]==a:
                    stac.pop()
                    ans.append('-')
                    break
                else:
                    print('NO')
                    return
    print(*ans,sep='\n')
sol()