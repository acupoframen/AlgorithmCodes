import sys
n,m,b=map(int,input().split())
input=sys.stdin.readline
data=[list(map(int,input().split())) for _ in range(n)]
answer=[]
for num in range(0,257):
    func1=0
    func2=0
    for i in range(n):
        for j in range(m):
            if data[i][j]<num:
                func1-=data[i][j]-num
            else:
                func2+=data[i][j]-num
    if b-func1+func2>=0:
        answer.append([2*func2+func1,num])
answer.sort(key=lambda x:(x[0],-x[1]))
print(*answer[0])