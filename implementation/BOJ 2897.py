r,c=map(int,input().split())
data=list(list(input()) for _ in range(r))
answer=list(0 for _ in range(5))
for i in range(r-1):
    for j in range(c-1):
        temp=[data[i][j],data[i+1][j+1],data[i+1][j],data[i][j+1]]
        if "#" not in temp:
            answer[temp.count("X")]+=1

for i in range(5):
    print(answer[i])