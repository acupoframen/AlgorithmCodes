import sys
input= sys.stdin.readline
n,c=map(int,input().split())
data=list(map(int,input().split()))
datasum=sum(data[:c])
answer,idx=0,0
for i in range(n):
    if i<c:
        if 129<=sum(data[:i+1])<=138:
            answer+=1
    else:
        datasum+=data[i]
        datasum-=data[idx]
        idx+=1
        if 129<=datasum<=138:
            answer+=1

print(answer)