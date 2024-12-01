n,m,k,x,y=map(int,input().split())
data=list()
for _ in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
data.sort(key=lambda d: (d[0] * x - d[1] * y))
time1=k
time2=k
for i in range(m):
    time1+=data[i][0]
    time2-=data[i][1]
print(time1*x+time2*y)