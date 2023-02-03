n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
answer=0
data.append(data[0])
for i in range(n):
    area=0
    area+=(data[i][0]-data[0][0])*(data[i+1][1]-data[0][1])
    area-=(data[i+1][0]-data[0][0])*(data[i][1]-data[0][1])
    area/=2
    answer+=area
print(round(abs(answer),1))