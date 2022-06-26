import sys

def sol():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    min_val = abs(N-100)

    if M==0:
        print(min(min_val,len(str(N))))
        return

    broken = sys.stdin.readline().split()

    for num in range(1000001):
        snum = str(num)
        
        for i in range(len(snum)):
            if snum[i] in broken:
                break
            elif i==len(snum)-1:
                min_val = min(min_val, abs(num-N)+len(snum))
           
    print(min_val)
    

sol()