data=list(map(int,input().split()))
answer=[1,1,2,2,2,8]
for i in range(len(data)):
    print(answer[i]-data[i],end=" ")