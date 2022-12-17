name=list(input())
n=int(input())
data=[0]*3
for i in range(n):
    newName=input()
    for j in range(len(name)):
        if name[j]==newName[0]:
            data[j]+=1
if name[0]==name[1]==name[2]:
    print(int(data[0]*(data[0]-1)*(data[2]-2)/6))
elif name[0]==name[1]:
    print(int(data[0]*(data[1]-1)*data[2]/2))
elif name[1]==name[2]:
    print(int(data[0]*data[1]*(data[1]-1)/2))
elif name[2]==name[0]:
    print(int(data[0]*data[1]*(data[0]-1)/2))
else:
    print(int(data[0]*data[1]*data[2]))
