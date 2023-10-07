n=int(input())
data=list(map(int,input().split()))
data.sort()
answer=0
for i in range(len(data)):
    answer+=(len(data)-i)*data[i]

print(answer)