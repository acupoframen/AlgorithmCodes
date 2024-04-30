from copy import deepcopy
from itertools import permutations
data=list(list(input()) for _ in range(5))
star=[[0,4],[1,1],[1,3],[1,5],[1,7],[2,2],[2,6],[3,1],[3,3],[3,5],[3,7],[4,4]]
values=[]
missing=[chr(i+ord('A')) for i in range(12)]
missingSpots=[]

def ok(a,b,c,d):
    if ord(a)+ord(b)+ord(c)+ord(d)-ord('A')*4+4==26:
        return True
    else:
        return False
for i in range(12):
    values.append(data[star[i][0]][star[i][1]])
    if data[star[i][0]][star[i][1]]=='x':
        missingSpots.append(i)
    else:
        missing.remove(data[star[i][0]][star[i][1]])

for perm in permutations(missing,len(missing)):
    temp=deepcopy(values)
    for i in range(len(perm)):
        temp[missingSpots[i]]=perm[i]
    if ok(temp[0],temp[2],temp[5],temp[7]) and ok(temp[1],temp[2],temp[3],temp[4]) and ok(temp[7],temp[8],temp[9],temp[10]) and ok(temp[0],temp[3],temp[6],temp[10]) and ok(temp[4],temp[6],temp[9],temp[11]):
        for i in range(12):
            data[star[i][0]][star[i][1]]=temp[i]
        break
for i in data:
    print(*i,sep="")