data=list(map(int,input().split()))
n=int(input())
answer=0
for _ in range(n):
    temp=0
    for i in range(3):
        data1=list(map(int,input().split()))
        for j in range(3):
            temp+=data[j]*data1[j]
    answer=max(answer,temp)

print(answer)