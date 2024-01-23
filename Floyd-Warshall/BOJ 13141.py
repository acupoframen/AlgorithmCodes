n,m=map(int,input().split())
import math
mindata=list(list(math.inf for _ in range(n+1)) for _ in range(n+1))
maxdata=[[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s,e,l=map(int,input().split())

    mindata[s][e]=min(mindata[s][e],l)
    mindata[e][s]=min(mindata[e][s],l)

    maxdata[s][e]=max(maxdata[s][e],l)
    maxdata[e][s]=max(maxdata[e][s],l)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                continue
            mindata[i][j]=min(mindata[i][j],mindata[i][k]+mindata[k][j])

answer=math.inf
for s in range(1,n+1):
    temp=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i!=j:
                if not maxdata[i][j]:
                    continue
            if mindata[s][j] ==math.inf or mindata[s][i]==math.inf:
                continue
            if mindata[s][i]<mindata[s][j]:
                a,b=mindata[s][i],mindata[s][j]
            else:
                b,a=mindata[s][i],mindata[s][j]
            if maxdata[i][j]>=(b-a):
                temp=max(temp, b+ (maxdata[i][j]-(b-a))/2)
    answer=min(answer,temp)

print("%.1f" %answer) 
