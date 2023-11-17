import math
mil=1000001
minbro=[-1 for _ in range(mil)]
siscount=[0 for _ in range(mil)]
for i in range(2,mil):
    for j in range(i*2,mil,i):
        if minbro[j]==-1:
            minbro[j]=i
            siscount[j]+=1
        else:
            siscount[j]+=1
sistercountdivision=[[] for _ in range(mil)]
for i in range(2,mil):
    sistercountdivision[siscount[i]].append(i)

t=int(input())
for i in range(1,t+1):
    answer=0
    n,m=map(int,input().split())
    for j in (sistercountdivision[siscount[n]]):
        if j>=n:
            break
        if minbro[j]==-1:
            continue
        if minbro[j]>=m:
            answer+=1
    print("Case #", end="")
    print(i,end="")
    print(": ",end="")
    print(answer)