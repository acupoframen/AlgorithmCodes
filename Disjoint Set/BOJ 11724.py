n,m=map(int,input().split())
data= [i for i in range(n+1)]
def find(a):
    if data[a]!=a:
        data[a]=find(data[a])
    return data[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a>b:
            data[a]=b
        else:
            data[b]=a

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)
answer=[]
for i in data[1:]:
    answer.append(find(i))

print(len(set(answer)))