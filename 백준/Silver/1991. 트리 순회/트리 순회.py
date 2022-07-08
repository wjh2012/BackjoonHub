import sys

def preorder(c):
    global dfd
    if c=='.':
        return
    child = dfd[c]
    print(c,end='')
    preorder(child[0])
    preorder(child[1])
         
def inorder(c):
    global dfd
    if c=='.':
        return
    child = dfd[c]
    inorder(child[0])
    print(c,end='')
    inorder(child[1])


def postorder(c):
    global dfd
    if c=='.':
        return
    child = dfd[c]
    postorder(child[0])
    postorder(child[1])
    print(c,end='')
    

def sol():
    N = int(sys.stdin.readline())
    global dfd
    dfd = dict()
    for _ in range(N):
        node, left, right = sys.stdin.readline().split()
        dfd[node]=[left,right]
    
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')

sol()