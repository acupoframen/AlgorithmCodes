n,m=map(int,input().split())
pack=[]
solo=[]
for _ in range(m):
    a,b=map(int,input().split())
    pack.append(a)
    solo.append(b)
pack.sort()
solo.sort()
answer=0
if solo[0]<pack[0]/6:
    answer=solo[0]*n
elif pack[0]<solo[0]*(n%6):
    answer=(n//6+1)*pack[0]
else:
    answer=(n//6)*pack[0]+(n%6)*solo[0]
print(answer)