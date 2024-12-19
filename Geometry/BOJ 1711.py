n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            point1=data[i]
            point2=data[j]
            point3=data[k]
            d1=(point1[0]-point2[0])**2+(point1[1]-point2[1])**2
            d2=(point2[0]-point3[0])**2+(point2[1]-point3[1])**2
            d3=(point3[0]-point1[0])**2+(point3[1]-point1[1])**2
            if 2*max(d1,d2,d3)==d1+d2+d3:
                answer+=1
print(answer)