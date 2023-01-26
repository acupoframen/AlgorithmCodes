n=int(input())
data=list(map(int,input().split()))
answer=0
total=sum(data[1:n-1])
firstsum=total+data[n-1]
thirdsum=0
for i in range(1,n-1):
    firstsum-=data[i]
    thirdsum+=data[i-1]
    answer=max(answer,total-data[i]+data[-1]+firstsum)
    answer=max(answer,total+data[i])
    answer=max(answer,total-data[i]+thirdsum+data[0])
print(answer)