import sys
sys.setrecursionlimit(10**9)
def sol():
    node = []
    while True:
        try:
            node.append(int(sys.stdin.readline()))
        except:
            break

    def pre(start, end):
        if start>end:
            return

        fin = end+1

        for i in range(start+1, end+1):
            if node[start] < node[i]:
                fin = i
                break

        pre(start+1, fin-1)
        pre(fin, end)
        print(node[start])

    pre(0, len(node)-1)

sol()