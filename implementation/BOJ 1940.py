n=int(input())
m=int(input())
data=[0]*100001
data=list(map(int,input().split()))
answer=0
data.sort()
for i in data:
    if i>=m-i:
        break
    if m-i in data:
        answer+=1
print(answer)