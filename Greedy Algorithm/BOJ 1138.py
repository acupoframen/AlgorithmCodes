n=int(input())
data=list(map(int,input().split()))
answer=[0 for _ in range(n)]
for i in range(n):
    val=data[i]
    count=0
    for j in range(n):
        if answer[j]==0 and count==val:
            answer[j]=i+1
            break
        elif answer[j]==0:
            count+=1
for i in range(n):
    print(answer[i], end=' ')