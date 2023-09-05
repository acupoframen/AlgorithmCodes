n=int(input())
data=[]
for _ in range(n):
    data.append(list(input().split())[1:])
data.sort()
dashes='--'
answer=[]
for i in range(n):
    if i==0:
        for j in range(len(data[i])):
            answer.append(dashes*j+data[i][j])
    else:
        index=0
        for j in range(len(data[i])):
            if data[i-1][j]!=data[i][j] or len(data[i-1])<=j:
                break
            else:
                index=j+1
        for j in range(index,len(data[i])):
            answer.append(dashes*j+data[i][j])

for i in answer:
    print(i)