import sys
sys.setrecursionlimit(10**9)

def sol():
    n = int(sys.stdin.readline())
    inord = list(map(int,sys.stdin.readline().split()))
    postord = list(map(int,sys.stdin.readline().split()))

    # 인덱스 빨리 찾기
    rootIdx = [0]*(n+1)
    for i in range(n):
        rootIdx[inord[i]] = i
        
    def preorder(ins, ine, pos, poe):
        if ins > ine or pos>poe:
            return
        
        rootVal = postord[poe]
        ridx = rootIdx[rootVal]

        print(rootVal, end=' ')

        tmp = pos+ridx-ins

        Lins = ins
        Line = ridx-1
        Lpos = pos
        Lpoe = tmp-1
        if Lins <= Line and Lpos <=Lpoe:
            preorder(Lins, Line, Lpos, Lpoe)

        Rins = ridx+1
        Rine = ine
        Rpos = tmp
        Rpoe = poe-1
        if Rins <= Rine and Rpos <=Rpoe:
            preorder(Rins, Rine, Rpos, Rpoe)

    preorder(0,n-1,0,n-1)

sol()