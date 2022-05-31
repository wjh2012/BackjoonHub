n=int(input())
i=0
count=0

while True:
    if str(i).find('666')!=-1:
        count+=1
        if count==n:
            print(i)
            break
    i+=1