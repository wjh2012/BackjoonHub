import sys
def sol():
    k, n = map(int,sys.stdin.readline().split())
    a = [int(sys.stdin.readline()) for _ in range(k)]

    maxlen = sum(a)//n+1
    minlen = 1

    ans=0
    while True:
        half = (minlen+maxlen)//2

        if half == 1:
            print(1)
            break

        if ans!=0 and half==minlen:
            print(ans)
            break

        canMake=0
        # half의 길이로 만들수 있는 갯수
        for i in a:
            canMake+=(i//half)

        if canMake<n:
            maxlen=half
        elif canMake>=n:
            ans=half
            minlen=half
sol()