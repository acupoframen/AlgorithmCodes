import math
coord=list(map(int, input().split()))
q=int(input())
for _ in range(q):
    temp=list(map(int, input().split()))
    time=list(0 for _ in range(3))
    for i in range(3):
        time[i]=abs(temp[0]-coord[i*2])+abs(temp[1]-coord[i*2+1])
    answer=1e10
    for i in range(3):
        answer=min(answer,(math.ceil(time[i]/temp[i+2]))*temp[i+2])
    print(answer)