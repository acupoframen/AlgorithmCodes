g=int(input())
p=int(input())
data=[int(input()) for _ in range(p)]
parents=[int(i) for i in range(g+1)]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a
answer=0
for i in data:
    i=find(i)
    if i==0:
        break
    parents[i]=parents[i-1]
    answer+=1

print(answer)