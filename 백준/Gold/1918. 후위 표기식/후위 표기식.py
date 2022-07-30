import sys

def sol():
    S = sys.stdin.readline().rstrip()
    operdic = dict()
    operdic = {
        '(' : 0,
        ')' : 0,
        '*' : 2,
        '/' : 2,
        '+' : 1,
        '-' : 1
    }

    operator = ['(',')','*','/','+','-']
    stac = []
    ans = ''

    for i in S:
        # 문자 or 스택비어있음 or '('
        if i not in operator:
            ans+=i
        elif not stac or i == '(':
            stac.append(i)
        else:
            if i == ')':
                while stac[-1] != '(':
                    ans += stac.pop()
                stac.pop()
            else:
                s_prior = operdic[stac[-1]]
                i_prior = operdic[i]

                if s_prior < i_prior:
                    stac.append(i)
                else:
                    while s_prior >= i_prior:
                        ans += stac.pop()
                        if stac:
                            s_prior = operdic[stac[-1]]
                        else:
                            break
                    stac.append(i)
    while stac:
        ans += stac.pop()
    print(ans)   

sol()
