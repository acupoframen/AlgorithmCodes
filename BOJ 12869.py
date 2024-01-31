from itertools import permutations
n=int(input())
data=list(map(int,input().split()))
damagelist=[9,3,1]
damagelist=damagelist[:n]
damagepattern=list(permutations(damagelist,n))
def attack(data1,pat,c):
    global answer
    dampattern=damagepattern[pat]
    for i in range(n):
        data[i]-=dampattern[i]
    if all(i<0 for i in data):
        answer=min(answer,c)
    else:
        for i in range
answer=1e10
attack(data,i,0)
print(answer)