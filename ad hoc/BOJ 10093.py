a,b=map(int,input().split())
a,b=min(a,b),max(a,b)
if a==b:
    print(0)
    exit()      
print(b-a-1)
for i in range(a+1,b):
    print(i,end=' ')