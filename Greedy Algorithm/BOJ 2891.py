n,s,r=map(int,input().split())
data=list(map(int,input().split()))
extra=list(map(int,input().split()))
extrayacht =[0 for _ in range(n+1)]
for i in extra:
    extrayacht[i]=1
    if i in data:
        extrayacht[i]=0
        data.remove(i)
answer=0
for i in data:
    answer+=1
    for j in range(max(1,i-1),min(n+1,i+2)):
        if extrayacht[j]==1:
            extrayacht[j]=0
            answer-=1
            break
print(answer)