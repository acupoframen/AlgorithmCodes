from itertools import permutations
data=list(list(map(int,input().split())) for _ in range(4))
curr=data[0]
answer=1e10
for order in permutations(data[1:]):

    curr=data[0]
    temp=0
    for i in order:
        temp+=((curr[0]-i[0])**2+(curr[1]-i[1])**2)**0.5

        curr=i
    answer=min(temp,answer)

print("%d" %answer)