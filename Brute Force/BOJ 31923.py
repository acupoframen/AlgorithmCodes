import math
n,p,q=map(int,input().split())
data=[[] for _ in range(n)]
temp=list(map(int,input().split()))
maximum=0
for i in range(n):
    data[i].append(temp[i])
    maximum=max(maximum,temp[i])
temp=list(map(int,input().split()))
for i in range(n):
    data[i].append(temp[i])
answer=[0 for _ in range(n)]
total=0
for i in range(n):
    if p<q:
        if data[i][0]<data[i][1]:
            print("NO")
            exit(0)
        while data[i][0]!=data[i][1]:
            data[i][0]+=p
            data[i][1]+=q
            answer[i]+=1
            total+=1
            if total>10000:
                print("NO")
                exit(0)
    if p>q:
        if data[i][0]>data[i][1]:
            print("NO")
            exit(0)
        while data[i][0]!=data[i][1]:
            data[i][0]+=p
            data[i][1]+=q
            answer[i]+=1
            total+=1
            if total>10000:
                print("NO")
                exit(0)
    if p==q:
        if data[i][0]!=data[i][1]:
            print("NO")
            exit(0)

print("YES")
print(*answer)