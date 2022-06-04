def makeStar(n):
    if n==1:
        return ['*']

    stars=makeStar(n//3)
    result = []

    for star in stars:
        result.append(star*3)
    for star in stars:
        result.append(star+' '*(n//3)+star)
    for star in stars:
        result.append(star*3)
    return result
    
def sol():
    n = int(input())
    ans=makeStar(n)
    for i in ans:
        print(i)
sol()