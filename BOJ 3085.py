n=int(input())
data=list(list(input()) for _ in range(n))

answer=0
def check():
    maxtemp=1
    temp=1
    for i in range(n):
        for j in range(1,n):
            if data[i][j]==data[i][j-1]:
                temp+=1
            else:
                maxtemp=max(maxtemp,temp)
                temp=1
        maxtemp=max(maxtemp,temp)
        temp=1
    
    for j in range(n):
        for i in range(1,n):
            if data[i][j]==data[i-1][j]:
                temp+=1
            else:
                maxtemp=max(maxtemp,temp)
                temp=1
        maxtemp=max(maxtemp,temp)
        temp=1
    
    return maxtemp

for i in range(n):
    for j in range(n):
        if j+1<n:
            data[i][j],data[i][j+1]=data[i][j+1],data[i][j]
            answer=max(check(),answer)
            data[i][j],data[i][j+1]=data[i][j+1],data[i][j]
        if i+1<n:
            data[i][j],data[i+1][j]=data[i+1][j],data[i][j]
            answer=max(answer,check())
            data[i][j],data[i+1][j]=data[i+1][j],data[i][j]

print(answer)