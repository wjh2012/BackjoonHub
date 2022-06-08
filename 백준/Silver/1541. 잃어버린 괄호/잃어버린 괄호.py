import sys

def sol():
    s = sys.stdin.readline().rstrip()
    s=s.split('-')
    for i in range(len(s)):
        s[i]=list(map(int,s[i].split('+')))

    if len(s)>1:
        ac = 0
        for i in range(1,len(s)):
            ac+=sum(s[i])
        print(sum(s[0])-ac)
    else:
        print(sum(s[0]))

sol()