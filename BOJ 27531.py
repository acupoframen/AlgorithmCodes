n=int(input())
parent=[i for i in range(n+1)]

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a
data=[[] for _ in range(n+1)]
answer=0
for _ in range(n):
    a,b,c=map(int,input().split())
    if a==b:
        answer+=c
    elif find(a)==find(b):
        data[a]=[b,c]
        i=a
        answer1=0
        answer2=0
        temp=0
        while True:
        
        answer+=min(answer1,answer2)
    else:
        data[a]=[b,c]
        union(a,b)
print(answer)