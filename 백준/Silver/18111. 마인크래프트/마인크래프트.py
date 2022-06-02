import sys
import random

N, M, B = map(int,sys.stdin.readline().split())

a=[]
for _ in range(N):
    a.extend(list(map(int,sys.stdin.readline().split())))

maxHigh = (sum(a)+B)//(N*M)
if maxHigh>256:
    maxHigh=256
minHigh = min(a)
# 전처리 시간
abtime=0
# 절대 불가능한 블록 제거 (전처리)
for i in range(N*M):
    if a[i]>maxHigh:
        abtime+=(a[i]-maxHigh)*2 # 전처리 시간 추가
        B+=a[i]-maxHigh # 전처리 블록 인벤토리 추가
        a[i]=maxHigh

hili =[]
for high in range(minHigh, maxHigh+1):
    mytime=0
    for bloc in a:
        if bloc==high:
            continue

        if bloc>high:
            mytime+=(bloc-high)*2
        else:
            mytime+=(high-bloc)

    hili.append((abtime+mytime,high))

hili.sort(key=lambda x:-x[1])    
hili.sort(key=lambda x:x[0])

print(*hili[0])