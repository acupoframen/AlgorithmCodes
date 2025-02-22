n=int(input())
data=list(list(0 for _ in range(5)) for _ in range(3))
for i in range(3):
    data[i][4]=i+1
for _ in range(n):
    temp=list(map(int,input().split()))
    data[temp.index(3)][3]+=1
    data[temp.index(2)][2]+=1
    data[temp.index(1)][1]+=1
    data[temp.index(3)][0]+=3
    data[temp.index(2)][0]+=2
    data[temp.index(1)][0]+=1
data.sort(key=lambda x:(-x[0],-x[3],-x[2]))
if data[0][0]==data[1][0] and data[0][3]==data[1][3] and data[0][2]==data[1][2]:
    print(0,data[0][0])
else:
    print(data[0][4],data[0][0])