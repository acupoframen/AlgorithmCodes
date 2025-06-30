from itertools import combinations
n=int(input())
data=list(0 for _ in range(101))
for _ in range(n):
    temp=list(map(int,input().split()))
    for i in temp:
        data[i]+=1
answer=0
for temp in combinations(range(1, 101), 3):
    a,b,c=temp
    data[a]+=1
    data[b]+=1
    data[c]+=1
    for i in range(100,0,-1):
        if data[i]==1:
            if i in (a,b,c):
                answer+=1
            break
    data[a]-=1
    data[b]-=1
    data[c]-=1
print(answer)