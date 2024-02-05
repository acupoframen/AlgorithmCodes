t=int(input())
data=list(map(int,input().split()))
answer=[[0,0,0] for _ in range(int(1e5)+1)]
for i in range(1,int(1e5)+1):
    if not i%3:
        j=i//3
        answer[i][0]=3*j*(j+1)//2
    else:
        answer[i][0]=answer[i-1][0]
    if not i%7:
        j=i//7
        answer[i][1]=7*j*(j+1)//2
    else:
        answer[i][1]=answer[i-1][1]
    if not i%21:
        j=i//21
        answer[i][2]-=21*j*(j+1)//2
    else:
        answer[i][2]=answer[i-1][2]
for i in data:
    print(sum(answer[i]))