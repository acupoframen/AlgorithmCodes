from collections import deque
from itertools import permutations
from copy import deepcopy
n=int(input())
temperature=list(map(int,input().split()))
solution=list(map(int,input().split()))
answer=[[solution.index(1)+1,temperature[0]],[solution.index(2)+1,temperature[1]]]
log=[[[] for _ in range(101)] for _ in range(101)]
q=deque()
q.append([[1,100],[2,100],[]])
log[100][100].append([1,2])
while q:
    temp=q.popleft()
    if answer==temp[:2]:
        print(len(temp[2]))
        for i in temp[2]:
            print(*i)
        exit(0)
    if temp[0][1]<answer[0][1] or temp[1][1]<answer[1][1]:
        continue
    possible=[1,2,3]
    for i in possible:
        if temp[0][0]==i or temp[1][0]==i:
            continue
        for j in range(1,4):
            if j==temp[0][0] and [i,temp[1][0]] not in log[temp[0][1]-5][temp[1][1]]:
                log[temp[0][1]-5][temp[1][1]].append([i,temp[1][0]])
                q.append([[i,temp[0][1]-5],temp[1],temp[2]+[[j,i]]])
            elif j==temp[1][0] and [temp[0][0],i] not in  log[temp[0][1]][temp[1][1]-5]:
                log[temp[0][1]][temp[1][1]-5].append([temp[0][0],i])
                q.append([temp[0],[i,temp[1][1]-5],temp[2]+[[j,i]]])

print(-1)