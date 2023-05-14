n,k=map(int,input().split())
data=[0]+list(map(int,input().split()))
level=0
damage=0
robotCoord=[0 for _ in range(n+1)]
while True:
    level+=1
    damage=0
    datan=data[n]
    for i in range(n-1,0,-1):
        data[i+1]=data[i]
        robotCoord[i+1]=robotCoord[i]
        if i==n-1 and robotCoord[i+1]==1:
            robotCoord[i+1]=0
    robotCoord[1]=0
    data[1]=data[2*n]
    for i in range(2*n-1,n,-1):
        data[i+1]=data[i]
    data[n+1]=datan
    for i in range(n-1,0,-1):
        if robotCoord[i]==1 and robotCoord[i+1]==0:
            if data[i+1]!=0 :
                if i==n-1:
                    robotCoord[i]=0
                    robotCoord[n]=0
                    data[i+1]-=1
                else:
                    robotCoord[i+1]=1
                    robotCoord[i]=0
                    data[i+1]-=1
    if data[1]>0:
        robotCoord[1]=1
        data[1]-=1
    for i in range(1,2*n+1):
        if data[i]<=0:
            damage+=1
    if damage>=k:
        break

print(level)