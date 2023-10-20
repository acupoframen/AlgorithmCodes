n=int(input())
data=[]
for i in range(n):
    a,b=input().split()
    a=int(a)
    data.append([a,i,b])
data.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(data[i][0],data[i][2])