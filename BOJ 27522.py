data=[]
teamR=0
teamB=0
for i in range(8):
    time,team=input().split()
    a,b,c=time.split(":")
    data.append([a,b,c,team])
data.sort()
points=[10,8,6,5,4,3,2,1]
for i in range(0,8):
    if data[i][3]=='R':
        teamR+=points[i]
    else:
        teamB+=points[i]
if teamR>teamB:
    print("Red")
else:
    print("Blue")