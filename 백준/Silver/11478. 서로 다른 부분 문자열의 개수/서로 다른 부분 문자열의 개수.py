import sys
s=sys.stdin.readline().rstrip()
ans=set()
n=len(s)

end=n
while n:
    i=0
    while i+n<=end:
        ans.add(s[i:i+n])
        i+=1
    n-=1
print(len(ans))