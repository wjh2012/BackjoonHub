k = int(input())
ans = []

for _ in range(k):
    a = int(input())
    if a==0:
        ans.pop()
    else:
        ans.append(a)
        
print(sum(ans))