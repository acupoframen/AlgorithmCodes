import copy
import sys
input=sys.stdin.readline
n=int(input())
data=list(list(input().strip()) for _ in range(n))
answer=1e10
for bit in range(1<<n):
    temp=[data[i][:] for i in range(n)]
    for i in range(n):
        if bit&(1<<i):
            for j in range(n):
                if temp[i][j]=='H':
                    temp[i][j]='T'
                else:
                    temp[i][j]='H'
    tempsum=0
    for j in range(n):
        count=0
        for i in range(n):
            if temp[i][j]=='H':
                count+=1
        tempsum+=min(count,n-count)
    answer=min(answer,tempsum)
print(answer)