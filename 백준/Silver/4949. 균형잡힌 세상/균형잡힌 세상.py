import sys
a=[]
while True:
    s=sys.stdin.readline().rstrip()
    if s=='.':
        break
    a.append(s)

for i in a:
    stac = []

    for alp in i:
        if alp=='(' or alp=='[':
            stac.append(alp)

        elif alp==')':
            if stac:
                if stac[-1]=='(':
                    stac.pop()
                else:
                    break
            else:
                stac.append(alp)
                break
        elif alp==']':
            if stac:
                if stac[-1]=='[':
                    stac.pop()
                else:
                    break
            else:
                stac.append(alp)
                break
    if stac:
        print('no')
    else:
        print('yes')