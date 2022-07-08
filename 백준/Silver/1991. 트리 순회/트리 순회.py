import sys

def preorder(dfd,c):
    if c=='.':
        return
    child = dfd[c]
    print(c,end='')
    preorder(dfd,child[0])
    preorder(dfd,child[1])
         
def inorder(dfd,c):
    if c=='.':
        return
    child = dfd[c]
    inorder(dfd,child[0])
    print(c,end='')
    inorder(dfd,child[1])


def postorder(dfd,c):
    if c=='.':
        return
    child = dfd[c]
    postorder(dfd,child[0])
    postorder(dfd,child[1])
    print(c,end='')
    

def sol():
    N = int(sys.stdin.readline())
    dfd = dict()
    for _ in range(N):
        node, left, right = sys.stdin.readline().split()
        dfd[node]=[left,right]
    
    preorder(dfd,'A')
    print()
    inorder(dfd,'A')
    print()
    postorder(dfd,'A')

sol()