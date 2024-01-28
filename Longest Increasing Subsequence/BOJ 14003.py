import bisect,math
n=int(input())
data=list(map(int,input().split()))
lis=[-math.inf]
temp=[]
for i in data:
    if lis[-1]<i:
        temp.append([len(lis),i])
        lis.append(i)
    else:
        temp.append([bisect.bisect_left(lis,i),i])
        lis[bisect.bisect_left(lis,i)]=i
print(len(lis)-1)
answer=[]
idx=len(lis)-1
for i in range(len(temp)-1,-1,-1):
    if temp[i][0]==idx:
        answer.append(temp[i][1])
        idx-=1

print(*answer[::-1])