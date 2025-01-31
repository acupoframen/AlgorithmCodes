from itertools import combinations
data=list(map(int,input().split()))
answer=1e10
sum1=sum(data)
for i in combinations(data,2):
    answer=min(answer,abs(sum(i)-(sum1-sum(i))))
print(answer)