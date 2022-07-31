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

        preorder(ins, ridx-1, pos, pos+ridx-ins-1)
        preorder(ridx+1, ine, pos+ridx-ins, poe-1)

    preorder(0,n-1,0,n-1)

sol()