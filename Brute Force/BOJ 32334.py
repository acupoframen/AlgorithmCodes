import sys
input=sys.stdin.readline
n,d=map(int,input().split())
data=[1e10]+list([1e10]+list(map(int,input().split())) for _ in range(n))
answer=list(list(0 for _ in range(n+1)) for _ in range(n+1))

for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][j]==1:
            for x in range(max(1,i-d),min(n,i+d)+1):
                for y in range(max(1,j-d),min(n,j+d)+1):
                    answer[x][y]+=1
val=1e10
answerx=0
answery=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][j]:
            continue
        if answer[i][j]<val:
            answerx,answery=i,j
            val=answer[i][j]
            if answer[i][j]==0:
                print(answerx,answery)
                exit(0)
print(answerx,answery)
print(val)