n,x=map(int,input().split())
five=(x-1000*n)//4000
data=list(list(map(int,input().split())) for _ in range(n))
maxgap=sorted(data,reverse=True,key=lambda x: x[0]-x[1])
answer=0
for i in range(n):
    if i<=five-1 and maxgap[i][0]>maxgap[i][1]:
        answer+=maxgap[i][0]
    else:
        answer+=maxgap[i][1]
print(answer)