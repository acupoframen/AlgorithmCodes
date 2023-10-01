n,m=map(int,input().split())

data=[list(map(int,input().split())) for _ in range(n)]
already=[list(map(int,input().split())) for _ in range(m)]
table=[i for i in range(n+1)]
def find(a):
    if table[a]==a:
        return a
    else:
        table[a]=find(table[a])
    return table[a]

def union(a,b):
    a,b=find(a),find(b)
    if a>b:
        table[a]=b
    else:
        table[b]=a
dist=[]

for i in already:
    x,y=i
    union(x,y)
for i in range(n-1):
    for j in range(i+1,n):
        dist.append([i+1,j+1,((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2)**(1/2)])

answer=0
dist.sort(key=lambda x: x[2])
for i in dist:
    if find(i[0])!=find(i[1]):
        union(i[0],i[1])
        answer+=i[2]

print("%.2f" %answer)