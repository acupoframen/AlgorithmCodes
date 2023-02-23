n=int(input())
data=list(map(int,input().split()))
tf=list(map(int,input().split()))
print(sum(data))
answer=0
for i in range(n):
    if not tf[i]:
        answer+=data[i]
print(answer)