n=int(input())
data=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    data.append([a*100+b, c*100+d])
data.sort(key=lambda x: (x[0],x[1]))
target=301
answer=0
end=0
while True:
    if target>=1201 or len(data)==0 or target<data[0][0]:
        break
    for _ in range(len(data)):
        if len(data)==0:
            break
        if target>=data[0][0]:
            if end<=data[0][1]:
                end=data[0][1]
            del data[0]
        else:
            break
    target=end
    answer+=1
if target<1201:
    print(0)
else:
    print(answer)