n,x,y=map(int,input().split())
data=list(map(int,input().split()))
meal=0
waste=0
for i in data:
    div,mod=divmod(i,x)
    meal+=div
    waste+=max(0,mod-(y-x)*div)
print(meal)
print(waste)
