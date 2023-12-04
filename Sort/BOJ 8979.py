n,k=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
data.sort(key=lambda x: (x[1],x[2],x[3]),reverse=True)
place=1
temp=0
for i in range(n):
    if i==0:
        pass
    else:
        if data[i-1][1:]==data[i][1:]:
            temp+=1
        else:
            if temp!=0:
                place+=temp
                temp=0
            place+=1
    if data[i][0]==k:
        print(place)
        break