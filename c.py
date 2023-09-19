l=int(input())
n=int(input())
data=[0]*1001
answer=0
answerval=-1
fakeanswer=0
fakeanswerval=-1
for i in range(1,n+1):
    a,b=map(int,input().split())
    if fakeanswerval<(b-a):
        fakeanswer=i
        fakeanswerval=b-a
    va=0
    for j in range(a,b+1):
        if data[j] ==0:
            va+=1
            data[j]=1
    if answerval<va:
        answer=i
        answerval=va
print(fakeanswer)
print(answer)