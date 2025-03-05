n=int(input())
data=list(map(int,input().split()))
answer=0
for curr in range(n):
    curve=1e11
    temp=0
    for i in range(curr-1,-1,-1):
        tempcurve=(data[curr]-data[i])/abs(curr-i)
        if tempcurve<curve:
            temp+=1
            curve=tempcurve
    curve=-1e11
    for i in range(curr+1,n):
        tempcurve=(data[i]-data[curr])/abs(curr-i)
        if tempcurve>curve:
            temp+=1
            curve=tempcurve
    answer=max(answer,temp)
print(answer)