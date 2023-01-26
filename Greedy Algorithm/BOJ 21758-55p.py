n=int(input())
data=list(map(int,input().split()))
answer=0
total=sum(data[1:n-1])
for i in range(1,n-1):
    answer=max(answer,total-data[i]+data[-1]+sum(data[i+1:]))
    answer=max(answer,total+data[i])
    answer=max(answer,total-data[i]+sum(data[:i])+data[0])
print(answer)