n=int(input())
data=list(map(int,input().split()))
answer1=0
answer2=0
temp=0
for i in data:
    if i%2:
        temp+=1
    else:
        answer1+=temp
data.reverse()
temp=0
for i in data:
    if i%2:
        temp+=1
    else:
        answer2+=temp
print(min(answer1,answer2))