import sys
sys.setrecursionlimit(10**9)

def sol():
    # 전위 순회
    node = []
    while True:
        try:
            node.append(int(sys.stdin.readline()))
        except:
            break
    
    ans = []
    def post(s,e):
        if s>e:
            return

        pivot = e+1
        for i in range(s+1, e+1):
            if node[i] > node[s]:
                pivot = i
                break
        
        post(s+1, pivot-1)
        post(pivot, e)
        print(node[s])
        
    post(0, len(node)-1)

sol()