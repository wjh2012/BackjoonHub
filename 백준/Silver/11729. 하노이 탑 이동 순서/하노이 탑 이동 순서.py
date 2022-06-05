def hanoi(tower, target, ori, des, rem):
    if tower[ori][-1]==target:
        tower[des].append(tower[ori].pop())
        print(ori+1, des+1)
        return
    else:
        hanoi(tower, target-1, ori,rem,des)
        tower[des].append(tower[ori].pop())
        print(ori+1, des+1)
        hanoi(tower, target-1, rem, des, ori)

def sol():
    n = int(input())
    tower = [[x for x in range(n,0,-1)],[],[]]
    print(2**n-1)
    hanoi(tower,n,0,2,1)
    
sol()