from itertools import combinations
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=[]
answercount=0
for i,j in combinations(range(5),2):
    count=0
    for k in range(len(data)):
        if data[k][i]==data[k][j]==1:
            count+=1
    if answercount<=count:
        answercount=count
        answer=[i,j]
print(answercount)
for i in range(5):
    if i in answer:
        print("1",end=" ")
    else:
        print("0", end=" ")