n=int(input())
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a<=b:
        continue
    data.append([a,b])
data.sort()
maxval=0
maxi=0
for i in range(len(data)):
    a=data[i][0]
    temp=0
    for j in range(i,len(data)):
        if a>data[j][1]:
            temp+=(a-data[j][1])


    if temp>maxval:
        maxval=temp
        maxi=data[i][0]

print(maxi)