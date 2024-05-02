n,l,k=map(int,input().split())
data=[]
for i in range(n):
    a,b=map(int,input().split())
    if l>=b:
        data.append(140)
    elif l>=a:
        data.append(100)
data.sort(reverse=True)
answer=0
for i in range(min(k,len(data))):
    answer+=data[i]
print(answer)