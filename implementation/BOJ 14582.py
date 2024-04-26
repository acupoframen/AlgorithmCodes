data1=list(map(int,input().split()))
data2=list(map(int,input().split()))

score=0
flag=0
for i in range(9):
    score+=data1[i]
    if score>0:
        flag=1
    score-=data2[i]
if score<0 and flag==1:
    print("Yes")
else:
    print("No")