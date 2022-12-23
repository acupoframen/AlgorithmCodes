n=int(input())
data=[]
for _ in range(n):
    data.append(int(input()))
data.sort()
diffs=[]
for i in range(n-1):
    diffs.append(data[i+1]-data[i])
diffs.sort()
dist=1
for i in range(min(diffs),0,-1):
    flag=0
    for j in diffs:
        if j%i:
            flag=1
            break
    if not flag:
        dist=i
        break
    
answer=0
for i in diffs:
    answer+=(i//dist-1)

print(answer)
