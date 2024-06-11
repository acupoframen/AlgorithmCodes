import bisect
n=int(input())
data=list(map(int,input().split()))
answer=[data[0]]
for i in range(1,n):
    if data[i]>answer[-1]:
        answer.append(data[i])
    else:
        index=bisect.bisect_left(answer,data[i])
        answer[index]=data[i]
print(len(answer))