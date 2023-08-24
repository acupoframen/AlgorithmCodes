n,m,l,k=map(int,input().split())
data=[]
for _ in range(k):
    x,y=map(int,input().split())
    data.append([x,y])

answer=0
for i in range(len(data)):
    for j in range(len(data)):
        count=0
        for curr in range(len(data)):
            currx,curry=data[curr]
            if data[i][0]<=currx<=data[i][0]+l and data[j][1]<=curry<=data[j][1]+l:
                count+=1
        answer=max(answer,count)

print(k-answer)