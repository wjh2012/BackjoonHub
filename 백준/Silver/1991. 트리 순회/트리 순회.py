import sys
from collections import defaultdict

def preorder(dfd,c):
    if c=='.':
        return
    print(c,end='')
    preorder(dfd,dfd[c][0])
    preorder(dfd,dfd[c][1])
         
def inorder(dfd,c):
    if c=='.':
        return
    inorder(dfd,dfd[c][0])
    print(c,end='')
    inorder(dfd,dfd[c][1])


def postorder(dfd,c):
    if c=='.':
        return
    postorder(dfd,dfd[c][0])
    postorder(dfd,dfd[c][1])
    print(c,end='')
    

def sol():
    N = int(sys.stdin.readline())
    tree = [list(sys.stdin.readline().split()) for _ in range(N)]
    dfd = defaultdict(list)
    for i in tree:
        dfd[i[0]]=i[1:]

    preorder(dfd,'A')
    print()
    inorder(dfd,'A')
    print()
    postorder(dfd,'A')

sol()