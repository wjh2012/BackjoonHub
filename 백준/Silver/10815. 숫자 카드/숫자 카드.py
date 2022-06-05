import sys
sys.setrecursionlimit(15000)

def bns(arr, target, start, end):
    mid = (start+end)//2
    
    if arr[mid]==target:
        return 1
    elif mid==end:
        return 0
    elif arr[mid]>target:
        return bns(arr,target, start, mid-1)
    elif arr[mid]<target:
        return bns(arr,target, mid+1, end)

def sol():
    n = int(sys.stdin.readline().rstrip())
    card = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline().rstrip())
    num = list(map(int,sys.stdin.readline().split()))
    
    card.sort()
    
    ans = []
    
    for i in num:
        ans.append(bns(card, i, 0, n-1))
    
    print(*ans)
            
sol()
