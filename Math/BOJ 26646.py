n=int(input())
data=list(map(int,input().split()))
mo=[]
x=0
for i in range(n-1):
    mo.append((data[i]-data[i+1])**2+(data[i]+data[i+1])**2)

print(sum(mo))