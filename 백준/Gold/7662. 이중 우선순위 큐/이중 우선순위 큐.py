import sys
import heapq
from collections import defaultdict

def sol():
    T = int(sys.stdin.readline())
    for _ in range(T):
        k = int(sys.stdin.readline())

        maxHeap=[]
        minHeap=[]
        dic=defaultdict(int)

        for _ in range(k):
            comm, num = sys.stdin.readline().split()
            num = int(num)
            if comm=='I':
                heapq.heappush(minHeap,num)
                heapq.heappush(maxHeap,-num)
                dic[num]+=1
            elif comm=='D':
                if num==-1 and minHeap:
                    t=heapq.heappop(minHeap)
                    dic[t]-=1
                    while maxHeap and dic[-maxHeap[0]]<=0:
                        heapq.heappop(maxHeap)
                    while minHeap and dic[minHeap[0]]<=0:
                        heapq.heappop(minHeap)
                    
                elif num==1 and maxHeap:
                    t=heapq.heappop(maxHeap)
                    dic[-t]-=1
                    while maxHeap and dic[-maxHeap[0]]<=0:
                        heapq.heappop(maxHeap)
                    while minHeap and dic[minHeap[0]]<=0:
                        heapq.heappop(minHeap)

        while maxHeap and dic[-maxHeap[0]]<=0:
                        heapq.heappop(maxHeap)
        while minHeap and dic[minHeap[0]]<=0:
                        heapq.heappop(minHeap)
        
        if maxHeap and minHeap:
            big,small=0,0
            for i in maxHeap:
                if dic[-i]>0:
                    big=-i
                    break

            for i in minHeap:
                if dic[i]>0:
                    small=i
                    break

            print(big,small)
        else:
            print('EMPTY')
sol()