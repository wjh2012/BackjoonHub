import sys

def bns(arr, target, start, final):
    mid = (start+final)//2

    if arr[mid]==target:
        return mid

    if arr[mid]>target:
        return bns(arr,target,start,mid-1)
    elif arr[mid]<target:
        return bns(arr,target,mid+1,final)

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

seta = set(a)
aa = sorted(list(seta))

ans = []
for i in a:
    ans.append(bns(aa,i,0,len(aa)-1))

print(*ans)