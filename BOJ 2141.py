n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
data.sort()
ppl=0
for i in range(n):
    ppl+=data[i][1]
count=0
for i in range(n):
    count+=data[i][1]
    if count>=ppl/2:
        print(data[i][0])
        break