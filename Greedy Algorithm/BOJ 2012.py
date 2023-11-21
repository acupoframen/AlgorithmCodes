n=int(input())
data=[0]
for i in range(n):
    data.append(int(input()))
newdata=sorted(data)
answer=0
for i in range(1,n+1):
    answer+=abs(newdata[i]-i)
print(answer)