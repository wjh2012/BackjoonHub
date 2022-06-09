import heapq, sys

def sol():
    n = int(sys.stdin.readline())
    heap=[]
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x==0:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
        else:
            heapq.heappush(heap,(abs(x),x))

sol()