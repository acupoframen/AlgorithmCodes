import math
n,m=map(int,input().split())
data=list(list(input()) for _ in range(n))
answer=-1

for i in range(n):
    for j in range(m):
        for k in range(-n,n):
            for l in range(-m,m):
                s=""
                x,y=i,j
                if k==0 and l==0:
                    continue
                while 0<=x<n and 0<=y<m:
                    s+=data[x][y]
                    if math.sqrt(int(s)).is_integer():
                        answer=max(answer,int(s))
                    x+=k
                    y+=l
print(answer)