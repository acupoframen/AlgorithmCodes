n=int(input())
data=list(map(int,input().split()))
answer=0
for i in range(n):
    temp=0
    for j in range(n):
        if i==j:
            continue
        temp^=data[j]
    for j in range(data[i]):
        if temp^j==0:
            answer+=1
print(answer)