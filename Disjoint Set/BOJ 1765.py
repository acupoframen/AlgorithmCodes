n=int(input())
m=int(input())
parents=[i for i in range(n+1)]
def find(a):
    if parents[a]!=a:
        parents[a]=find(parents[a])
    return parents[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b
e=[[] for _ in range(n+1)]
f=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    if a=='E':
        e[c].append(b)
        e[b].append(c)
    else:
        f[c].append(b)
        f[b].append(c)
        union(b,c)

for i in range(1,n+1):
    for j in range(len(e[i])):
        for k in range(len(e[i])):
            union(e[i][j],e[i][k])
    for j in range(len(f[i])):
        for k in range(len(f[i])):
            union(f[i][j],f[i][k])

answer=0
for i in range(1,n+1):
    if find(i)==i:
        answer+=1

print(answer)