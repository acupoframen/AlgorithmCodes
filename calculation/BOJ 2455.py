data=[]
for i in range(4):
    data.append(list(map(int,input().split())))
maxNum=0
currentCount=0
for i in range(4):
    currentCount=currentCount+data[i][1]-data[i][0]
    maxNum=max(maxNum,currentCount)
print(maxNum)
