from itertools import combinations
n=int(input())
data=list(map(int,input().split()))

num=sum(data)

answer=set()

for i in range(1,n+1):
    for j in combinations(data,i):
        answer.add(sum(j))

print(num-len(answer))