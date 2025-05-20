n=int(input())
data=list(map(int,input().split()))
week=[0]*7
week[0]=1 #week 4= fri
for i in data:
    weektemp=week[:]
    for j in range(7):
        if weektemp[j]:
            week[(i+j)%7]=weektemp[j]    

if week[4]:
    print("YES")
else: 
    print("NO")