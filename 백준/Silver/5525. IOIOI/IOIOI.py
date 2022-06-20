import sys
          
def sol():
    N=int(input())
    M=int(input())
    S=sys.stdin.readline().rstrip()

    pi=[0,0,1]
    pat = 'IOI'+'OI'*(N-1)
    
    if N>1:
        pi.extend([x for x in range(2,N*2)])

    ans = 0
    t = 0
    for i in range(M):
        while t>0 and S[i]!=pat[t]:
            t=pi[t-1]
        if S[i]==pat[t]:
            if t==len(pat)-1:
                ans+=1
                t = pi[t]
            else:
                t+=1
    print(ans)

sol()