import math
n=int(input())
s = str(math.factorial(n))[::-1]
count=0
for i in s:
    if i=='0':
        count+=1
    else:
        break
print(count)