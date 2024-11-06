n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))

answer=0
for i in range(n):
    for j  in range(i+1,n):
        for k in range(j+1,n):
            a=((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2)**0.5
            b=((data[i][0]-data[k][0])**2+(data[i][1]-data[k][1])**2)**0.5
            c=((data[k][0]-data[j][0])**2+(data[k][1]-data[j][1])**2)**0.5
            s=(a+b+c)/2
            answer=max(answer,(s*(s-a)*(s-b)*(s-c))**0.5)
print(answer)