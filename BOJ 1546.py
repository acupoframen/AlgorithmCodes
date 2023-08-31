n=int(input())
data=list(map(int,input().split()))
maxVal=max(data)
newdata=[]
for i in range(n):
    newdata.append(data[i]/maxVal*100)
print(sum(newdata)/n)