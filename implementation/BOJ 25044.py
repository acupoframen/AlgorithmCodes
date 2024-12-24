n,k=map(int,input().split())
data=[]
currtime=-3*60
uptime=[180,180,18*60]
count=2
while currtime<(n+1)*60*24:
    currtime+=uptime[count]
    if (n+1)*60*24>currtime>=n*60*24:
        data.append(currtime)
    
    count+=1
    if count==2:
        
        currtime+=k
    if count==3:
        count=0

print(len(data))
for i in data:
    print("%02d:%02d" %(i//60%24,i%60))