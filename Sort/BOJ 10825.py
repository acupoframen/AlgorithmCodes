n=int(input())
data=[]
for i in range(n):
    name,a,b,c=input().split()
    data.append([name,int(a),int(b),int(c)])
data.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for i in range(n):
    print(data[i][0])