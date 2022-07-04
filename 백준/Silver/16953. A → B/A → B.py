from collections import deque, defaultdict

def sol():
    A,B = map(int,input().split())

    dic = defaultdict(int)
    dq = deque([A])

    while dq:
        x = dq.popleft()
        
        if x==B:
            print(dic[x]+1)
            return

        i = x*2
        j = x*10+1

        if i <= B:
            dic[i]=dic[x]+1
            dq.append(i)
        if j <= B:
            dic[j]=dic[x]+1
            dq.append(j)
    
    print(-1)

sol()