from copy import deepcopy
n=int(input())
data=[0]+list(map(int,input().split()))
house=[0 for _ in range(n+1)]
for index,person in enumerate(data):
    house[person]=index
m=int(input())
for _ in range(m):
    left,right=map(int,input().split())
    temp=deepcopy(house)
    temp=temp[:left]+sorted(temp[left:right+1])+temp[right+1:]

    answer=[0 for _ in range(n+1)]
    for i,person in enumerate(temp):
        answer[person]=i
    print(*answer[1:])