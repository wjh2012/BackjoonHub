import sys
    
def sol():
    N, T = map(int,sys.stdin.readline().split())
    # 과목 공부 시간
    tList = []
    # 과목 점수
    sList = []

    for _ in range(N):
        t,s = map(int,sys.stdin.readline().split())
        tList.append(t)
        sList.append(s)
    
    MaxScore = [[0]*(T+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for t in range(1,T+1):
            # 시간이 초과하면 직전 과목(계산된 최대점수)
            if tList[i-1] > t:
                MaxScore[i][t] = MaxScore[i-1][t]
            # 가능한 시간이면
            # 직전 과목(계산된 최대점수) vs 현과목으로 얻는 점수 + 현과목만큼 시간을 뺀 시간에서의 최대점수
            else:
                MaxScore[i][t] = max(MaxScore[i-1][t], sList[i-1] + MaxScore[i-1][t-tList[i-1]])
    
    print(MaxScore[N][T])

sol()