n=int(input())
data=list(map(int,input().split()))
totalBudget=int(input())
highLimit=0

if totalBudget>=sum(data):
    print(max(data))
else:
    data.sort()
    while data:
        if data[0]*len(data)>totalBudget:
            highLimit+=totalBudget//len(data)
            break
        else:
            for i in range (len(data)-1,-1,-1):
                val=data[0]
                totalBudget-=data[0]
                data[i]-=data[0]
                
                if data[i]==0:
                    del data[i]
            highLimit+=val
            if not data:
                break
    print(highLimit)
