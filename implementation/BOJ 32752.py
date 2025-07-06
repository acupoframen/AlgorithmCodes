n,l,r=map(int,input().split())
data=list(map(int,input().split()))
l-=1
r-=1
temp=data[:l]+sorted(data[l:r+1])+data[r+1:]
if sorted(data)==temp:
    print(1)
else:
    print(0)