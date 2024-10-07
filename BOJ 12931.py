n=int(input())
data=list(map(int,input().split()))
count=[[0,0] for _ in range(n)]
for i in range(n):
    while data[i]>0:
        if data[i]%2==0:
            data[i]//=2
            count[i][0]+=1
        else:
            data[i]-=1
            count[i][1]+=1
answer1=0
answer2=0
for i in range(n):
    answer1=max(answer1,count[i][0])
    answer2+=count[i][1]
print(answer1+answer2)