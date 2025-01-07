n,m=map(int,input().split())
data=[]
totalweight=0
weight=[0 for _ in range(n+1)]
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b]) #무게, 가격
    totalweight+=a 
if totalweight<m:
    print(-1)
else:
    data.sort(key=lambda x:(x[1],-x[0]))
    answer=1e12
    count=1
    for i in range(len(data)):
        price=data[i][1]
        if i and price==data[i-1][1]:
            count+=1
        else:
            count=1
        weight[i]=weight[i-1]+data[i][0]
        if weight[i]>=m:
            answer=min(answer,price*count)
    print(answer)