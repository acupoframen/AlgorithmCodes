n=int(input())
crane=list(map(int,input().split()))
m=int(input())
box=list(map(int,input().split()))
time=0
crane.sort(reverse=True)
box.sort(reverse=True)
if crane[0]<box[0]:
    print(-1)
    exit(0)
while len(box)>0:
    time+=1
    for i in range(n):
        for j in range(len(box)):
            if crane[i]>=box[j]:
                box.pop(j)
                break
    
print(time)