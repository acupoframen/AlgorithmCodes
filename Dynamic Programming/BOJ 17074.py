n=int(input())
data=[-1e10]+list(map(int,input().split()))+[1e10]
down=0
pos=0
for i in range(1,n+1):
    if data[i-1]>data[i]:
        down+=1
        pos=i
if not down:
    print(n)
elif down==1:
    answer=0
    if data[pos-1]<=data[pos+1]:
        answer+=1
    if data[pos-2]<=data[pos]:
        answer+=1
    print(answer)
else:
    print(0)