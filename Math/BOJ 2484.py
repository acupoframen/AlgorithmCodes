n=int(input())
answer=0
for _ in range(n):
    data=[0 for _ in range(7)]
    temp=list(map(int,input().split()))
    for i in temp:
        data[i]+=1
    if max(data)==4:
        answer=max(answer,data.index(4)*5000+50000)
    elif max(data)==3:
        answer=max(answer,data.index(3)*1000+10000)
    elif len(set(temp))==4:
        answer=max(answer,max(temp)*100)
    else:
        if len(set(temp))==2:
            temp.sort()
            answer=max(answer,2000+temp[0]*500+temp[3]*500)
        else:
            answer=max(answer,1000+data.index(2)*100)

print(answer)