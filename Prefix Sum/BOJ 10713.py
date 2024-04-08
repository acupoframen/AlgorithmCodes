n,m=map(int,input().split())
cities=list(map(int,input().split()))
data=[0]+list(list(map(int,input().split())) for _ in range(n-1))
answer=[0 for _ in range(n+1)]
for i in range(m-1):
    answer[min(cities[i:i+2])]+=1
    answer[max(cities[i:i+2])]-=1
for i in range(1,n):
    answer[i+1]+=answer[i]
answerval=0
for i in range(1,n):
    if data[i][0]*answer[i]>=data[i][1]*answer[i]+data[i][2]:
        answerval+=data[i][1]*answer[i]+data[i][2]
    else:
        answerval+=data[i][0]*answer[i]
print(answerval)