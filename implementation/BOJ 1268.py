n=int(input())
student=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    student.append(temp)

answer=list(list(0 for _ in range(n)) for _ in range(n))
for i in range(5):
    for j in range(n):
        for k in range(j+1,n):
            if student[j][i]==student[k][i]:
                answer[j][k]=1
                answer[k][j]=1

sol=1
ans=0
for i in range(len(answer)):
    if ans<sum(answer[i]):
        ans=sum(answer[i])
        sol=i+1
print(sol)