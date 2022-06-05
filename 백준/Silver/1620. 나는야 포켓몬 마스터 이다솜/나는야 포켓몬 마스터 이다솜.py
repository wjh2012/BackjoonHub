import sys

def sol():
    n,m=map(int,sys.stdin.readline().split())
    poke={}
    prob=[]

    #이름:순번
    for i in range(n):
        poke[sys.stdin.readline().rstrip()]=i+1
    name = list(poke.keys())

    for _ in range(m):
        tmp = sys.stdin.readline().rstrip()
        if ord(tmp[0]) in range(65,123):
            prob.append(tmp)
        else:
            prob.append(int(tmp))
        
    for i in prob:
        if type(i)==int:
            print(name[i-1])
        else:
            print(poke[i])
    
sol()