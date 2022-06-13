import sys

def sol():
    N=int(sys.stdin.readline())
    a=[]
    for _ in range(N):
        a.append(tuple(map(int,sys.stdin.readline().split())))
    a.sort(key=lambda x:x[0])
    a.sort(key=lambda x:x[1])
    
    last = 0
    answer = 0
    for i,j in a:
        if i>=last:
            answer+=1
            last=j

    print(answer)
sol()