n=int(input())
data=[]
for i in range(1,n+1):
    x,y,v=map(int,input().split())
    dist=((x**2)+(y**2))**0.5 /v
    data.append([i,dist])

data.sort(key= lambda x: x[1])

for i in data:
    print(i[0])