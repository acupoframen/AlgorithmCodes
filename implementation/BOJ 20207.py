n=int(input())
data=[0 for _ in range(366)]
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        data[i]+=1

depth=0
start=1
answer=0
for i in range(1,366):
    if i==365 and data[365]:
        depth=max(depth,data[i])
        answer+=(depth*((i+1)-start))
        break
    if not data[i]:
        answer+=(depth*((i)-start))
        start=i+1
        depth=0
    else:
        depth=max(depth,data[i])

print(answer)